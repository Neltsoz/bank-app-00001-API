from collections.abc import Sequence

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.schemas.account import AccountResponse


async def get_user_accounts(
    db: AsyncSession,
    user: User | None = None,
    user_id: int | None = None
) -> Sequence[AccountResponse]:
    if user is None:
        user_ = await db.execute(
            select(User).where(User.id == user_id)
        )
        user = user_.scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=404)
        
    await db.refresh(user, ['accounts'])
    return user.accounts
