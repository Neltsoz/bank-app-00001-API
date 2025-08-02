from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.payment import WebhookPayload
from app.services.payment import (
    process_payment
)


router = APIRouter()


@router.post('/by_webhook')
async def set_new_payment(
    webhook_payload: WebhookPayload,
    db: AsyncSession = Depends(get_db)
):
    return await process_payment(db, webhook_payload)
