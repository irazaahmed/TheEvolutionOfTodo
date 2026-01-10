from sqlmodel import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from typing import AsyncGenerator
from app.core.config import settings
import urllib.parse


# Create async engine - handling both PostgreSQL and SQLite with proper async drivers
database_url = settings.database_url

# Parse the URL to handle query parameters correctly
parsed_url = urllib.parse.urlparse(database_url)

# Determine the appropriate async driver based on the scheme
if parsed_url.scheme == 'postgresql':
    # Use asyncpg driver for PostgreSQL
    database_url = database_url.replace('postgresql://', 'postgresql+asyncpg://', 1)
elif parsed_url.scheme == 'sqlite':
    # Use aiosqlite driver for SQLite
    database_url = database_url.replace('sqlite:///', 'sqlite+aiosqlite:///', 1)

async_engine = create_async_engine(
    database_url,
    echo=False,  # Set to True for SQL query logging
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=300,  # Recycle connections after 5 minutes
    # Additional async-specific options
    pool_pre_ping=True,
    pool_recycle=300,
    pool_timeout=40,
    max_overflow=0,
)

# Create sync engine (for Alembic migrations, if needed)
sync_db_url = settings.database_url.replace('+asyncpg', '').replace('+aiosqlite', '')
sync_engine = create_engine(
    sync_db_url,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=300,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(async_engine) as session:
        yield session