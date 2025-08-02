from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.services.admin import create_main_admin


router = APIRouter()


@router.post('/init')
async def initiate_admin(
    db: AsyncSession = Depends(get_db)
):
    return await create_main_admin(db)
