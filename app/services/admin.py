from fastapi import (
    Response,
    status
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.config import (
    ADMIN_PASSWORD,
    ADMIN_EMAIL,
    ADMIN_NAME
)
from app.utils.security import get_password_hash


async def create_main_admin(db: AsyncSession) -> None:
    user = await db.execute(
        select(User).where(User.email == ADMIN_EMAIL)
    )
    user = user.scalar_one_or_none()

    if not user:
        admin = User(
            full_name=ADMIN_NAME,
            email=ADMIN_EMAIL,
            hashed_password=get_password_hash(ADMIN_PASSWORD),
            is_admin=True
        )

        db.add(admin)
        await db.commit()

        return Response(status_code=status.HTTP_201_CREATED)
    
    return Response(status_code=status.HTTP_400_BAD_REQUEST)
