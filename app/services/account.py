from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


async def get_user_accounts(
    user: User,
    db: AsyncSession
):
    await db.refresh(user, ['accounts'])
    return user.accounts
