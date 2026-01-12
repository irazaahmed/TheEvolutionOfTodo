from sqlmodel import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from typing import AsyncGenerator
from app.core.config import settings
import urllib.parse


# Create async engine - handling both PostgreSQL and SQLite with proper async drivers
original_database_url = settings.database_url

# Parse the URL to handle query parameters correctly
parsed_url = urllib.parse.urlparse(original_database_url)

# Determine the appropriate async driver based on the scheme
if parsed_url.scheme == 'postgresql':
    # Use asyncpg driver for PostgreSQL
    # We need to handle parameters separately for asyncpg compatibility

    # Parse query parameters to identify which ones are supported by asyncpg
    query_params = urllib.parse.parse_qs(parsed_url.query)

    # Remove the query parameters from URL construction for now
    # and handle them via connect_args
    base_url_without_params = parsed_url._replace(query='')
    base_url_str = urllib.parse.urlunparse(base_url_without_params)

    # The actual URL for asyncpg should not have the problematic query params
    database_url = base_url_str.replace('postgresql://', 'postgresql+asyncpg://', 1)

    # Prepare connect_args for asyncpg with supported SSL settings if needed
    connect_args = {}

    # Handle SSL if specific parameters were provided in the original URL
    if 'sslmode' in query_params or 'require' in original_database_url.lower():
        # asyncpg handles SSL automatically, but we can set it explicitly if needed
        # SSL is typically handled by asyncpg automatically when connecting to secured servers
        pass

    async_engine = create_async_engine(
        database_url,
        echo=False,  # Set to True for SQL query logging
        pool_pre_ping=True,  # Verify connections before use
        pool_recycle=300,  # Recycle connections after 5 minutes
        pool_timeout=40,
        max_overflow=0,
        connect_args=connect_args,  # Pass any necessary connection arguments here
    )
elif parsed_url.scheme == 'sqlite':
    # Use aiosqlite driver for SQLite
    database_url = original_database_url.replace('sqlite:///', 'sqlite+aiosqlite:///', 1)
    async_engine = create_async_engine(
        database_url,
        echo=False,  # Set to True for SQL query logging
        pool_pre_ping=True,  # Verify connections before use
        pool_recycle=300,  # Recycle connections after 5 minutes
        pool_timeout=40,
        max_overflow=0,
    )
else:
    # Default to original behavior for other schemes
    database_url = original_database_url
    if 'postgresql' in original_database_url:
        database_url = database_url.replace('postgresql://', 'postgresql+asyncpg://', 1)
    async_engine = create_async_engine(
        database_url,
        echo=False,  # Set to True for SQL query logging
        pool_pre_ping=True,  # Verify connections before use
        pool_recycle=300,  # Recycle connections after 5 minutes
        pool_timeout=40,
        max_overflow=0,
    )

# Create sync engine (for Alembic migrations, if needed)
# Process the original URL for the sync engine
sync_parsed_url = urllib.parse.urlparse(original_database_url)
if sync_parsed_url.scheme == 'postgresql':
    # For sync engine, we'll use the original URL but ensure it's in correct format
    sync_db_url = original_database_url.replace('+asyncpg', '').replace('+aiosqlite', '')

    # Handle sync engine connect_args separately if needed
    sync_connect_args = {}

    sync_engine = create_engine(
        sync_db_url,
        echo=False,
        pool_pre_ping=True,
        pool_recycle=300,
        pool_timeout=40,
        connect_args=sync_connect_args,
    )
elif sync_parsed_url.scheme == 'sqlite':
    sync_db_url = original_database_url
    sync_engine = create_engine(
        sync_db_url,
        echo=False,
        pool_pre_ping=True,
        pool_recycle=300,
        pool_timeout=40,
    )
else:
    sync_db_url = original_database_url.replace('+asyncpg', '').replace('+aiosqlite', '')
    sync_engine = create_engine(
        sync_db_url,
        echo=False,
        pool_pre_ping=True,
        pool_recycle=300,
        pool_timeout=40,
    )


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(async_engine) as session:
        yield session