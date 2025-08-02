from collections.abc import Sequence

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.utils.webhook import verify_webhook_signature
from app.models.payment import Payment
from app.models.account import Account
from app.models.user import User
from app.schemas.payment import (
    WebhookPayload,
    PaymentResponse
)


async def process_payment(
    db: AsyncSession, 
    payment_data: WebhookPayload
) -> PaymentResponse:
    if not verify_webhook_signature(payment_data):
        raise HTTPException(
            status_code=403
        )
    
    account = await db.execute(
        select(Account).where(Account.id == payment_data.account_id)
    )
    account = account.scalar_one_or_none()

    if not account:
        user = await db.execute(
            select(User).where(User.id == payment_data.user_id)
        )
        if not user.scalar_one_or_none():
            raise HTTPException(
                status_code=400
            )
        
        account = Account(
            id=payment_data.account_id,
            user_id=payment_data.user_id,
            balance=0
        )

        db.add(account)
        await db.commit()
        await db.refresh(account)
    
    payment = Payment(
        amount = payment_data.amount,
        user_id = payment_data.user_id,
        account_id = payment_data.account_id,
        signature=payment_data.signature
    )

    if account.user_id != payment_data.user_id:
        raise HTTPException(
            status_code=400
        )

    db.add(payment)

    account.balance += payment_data.amount

    try:
        await db.commit()
        await db.refresh(payment)
        await db.refresh(account)
        return payment
    
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=500
        )


async def get_user_payments(
    db: AsyncSession,
    user: User | None = None,
    user_id: int | None = None,
) -> Sequence[PaymentResponse]:
    if user is None:
        user_ = await db.execute(
            select(User).where(User.id == user_id)
        )
        user = user_.scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=404)
        
    await db.refresh(user, ['payments'])
    return user.payments
