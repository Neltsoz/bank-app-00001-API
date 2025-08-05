from collections.abc import Sequence

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
    destroy_user,
    get_all_users
)
from app.services.account import get_user_accounts
from app.services.payment import get_user_payments
from app.schemas.user import (
    UserCreate,
    UserResponse
)
from app.models.user import User
from app.utils.security import (
    get_current_admin,
    get_current_user
)
from app.schemas.payment import PaymentResponse
from app.schemas.account import AccountResponse


router = APIRouter()


@router.post('/')
async def new_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
) -> UserResponse:
    return await create_user(db, user_data)


@router.get('/')
async def get_users(
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
) -> Sequence[UserResponse]:
    return await get_all_users(db)


@router.get('/{user_id}')
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
) -> UserResponse:
    return await retrieve_user(user_id, db)


@router.get('/me/accounts')
async def get_my_accounts(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Sequence[AccountResponse]:
    return await get_user_accounts(db, user=user)


@router.get('/{user_id}/accounts')
async def get_user_s_accounts(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
) -> Sequence[AccountResponse]:
    return await get_user_accounts(db, user_id=user_id)


@router.get('/me/payments')
async def get_my_payments(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Sequence[PaymentResponse]:
    return await get_user_payments(db, user=user)


@router.get('/{user_id}/payments')
async def get_user_s_payments(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
) -> Sequence[PaymentResponse]:
    return await get_user_payments(db, user_id=user_id)


@router.put('/{user_id}')
async def update_user_data(
    user_id: int,
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
) -> UserResponse:
    return await update_user(user_id, db, user_data)


@router.delete('/{user_id}')
async def destroy_user_data(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: User = Depends(get_current_admin)
):
    return await destroy_user(user_id, db)
