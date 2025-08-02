from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.user import User
from app.utils.security import (
    get_current_user,
    get_current_admin
)
from app.schemas.payment import WebhookPayload
from app.services.payment import (
    process_payment,
    get_user_payments
)


router = APIRouter()


@router.post('/by_webhook')
async def set_new_payment(
    webhook_payload: WebhookPayload,
    db: AsyncSession = Depends(get_db)
):
    return await process_payment(db, webhook_payload)
