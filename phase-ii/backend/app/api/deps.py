from typing import AsyncGenerator
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.database import get_async_session
from fastapi import Depends


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async for session in get_async_session():
        yield session