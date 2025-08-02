from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.services.user import (
    create_user,
    retrieve_user,
    update_user,
    destroy_user
)
from app.services.account import get_user_accounts
from app.services.payment import get_user_payments
from app.schemas.user import UserCreate
from app.models.user import User
from app.utils.security import (
    get_current_admin,
    get_current_user
)


router = APIRouter()


@router.post('/')
async def new_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
):
    return await create_user(db, user_data)


@router.get('/')
async def get_users(
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
):
    return (await db.execute(select(User))).scalars().all()


@router.get('/{user_id}')
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
):
    return await retrieve_user(user_id, db)


@router.get('/me/accounts')
async def get_my_accounts(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await get_user_accounts(user, db)


@router.get('/{user_id}/accounts')
async def get_user_s_accounts(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
):
    user = await db.execute(select(User).where(User.id == user_id))
    user = user.scalar_one()
    return await get_user_accounts(user, db)


@router.get('/me/payments')
async def get_my_payments(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await get_user_payments(user, db)


@router.get('/{user_id}/payments')
async def get_user_s_payments(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
):
    user = await db.execute(select(User).where(User.id == user_id))
    user = user.scalar_one()
    return await get_user_payments(user, db)


@router.put('/{user_id}')
async def update_user_data(
    user_id: int,
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
):
    return await update_user(user_id, db, user_data)


@router.delete('/{user_id}')
async def destroy_user_data(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
):
    return await destroy_user(user_id, db)
