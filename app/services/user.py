from collections.abc import Sequence

from fastapi import (
    HTTPException,
    status
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.schemas.user import (
    UserCreate,
    UserResponse
)
from app.utils.security import get_password_hash
from app.models.user import User


async def create_user(
    db: AsyncSession,
    user_data: UserCreate
) -> UserResponse:
    hashed_password = get_password_hash(user_data.password)
    user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        full_name=user_data.full_name,
        is_admin=user_data.is_admin
    )

    db.add(user)
    await db.commit()
    return user


async def update_user(
    user_id: int,
    db: AsyncSession,
    user_data: UserCreate
) -> UserResponse:
    hashed_password = get_password_hash(user_data.password)

    user = await db.execute(select(User).where(User.id == user_id))
    user = user.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=400)
    
    user.full_name = user_data.full_name
    user.hashed_password = hashed_password
    user.email = user_data.email
    user.is_admin = user_data.is_admin

    await db.commit()

    return user


async def destroy_user(
    user_id: int,
    db: AsyncSession
):
    user = await db.execute(select(User).where(User.id == user_id))
    user = user.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=404
        )

    await db.delete(user)
    await db.commit()

    return status.HTTP_204_NO_CONTENT


async def retrieve_user(
    user_id: int,
    db: AsyncSession
) -> UserResponse:
    user = await db.execute(select(User).where(User.id == user_id))
    user = user.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=404
        )
    
    return user


async def get_all_users(
    db: AsyncSession
) -> Sequence[UserResponse]:
    return (await db.execute(select(User))).scalars().all()
