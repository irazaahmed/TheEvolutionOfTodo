# Database Connection Strategy: Todo Backend

**Feature**: 1-backend-core
**Created**: 2026-01-09
**Status**: Design

## Overview

This document outlines the database connection strategy for the Todo application using SQLModel with Neon Serverless PostgreSQL. The strategy focuses on efficient connection management, proper session handling, and reliable migration processes.

## Connection Architecture

### Async Database Engine

**Technology**: SQLAlchemy AsyncEngine with asyncpg driver
**Configuration**:
- Connection pooling with min/max pool sizes optimized for serverless
- Connection timeout settings appropriate for Neon's serverless nature
- Proper async/await patterns to maintain FastAPI performance

### Session Management

**Pattern**: Context manager approach with FastAPI dependency injection
**Implementation**:
- Create database sessions per request using `async with`
- Automatic session cleanup after request completion
- Proper exception handling to ensure session closure

## Database Configuration

### Environment Variables
```
DATABASE_URL=postgresql+asyncpg://username:password@host:port/database_name
TEST_DATABASE_URL=sqlite+aiosqlite:///./test.db
DATABASE_POOL_SIZE=5
DATABASE_POOL_MAX_OVERFLOW=10
DATABASE_POOL_RECYCLE=300
DATABASE_POOL_TIMEOUT=30
```

### Connection Pool Settings
- **pool_size**: 5 (default connections kept alive)
- **max_overflow**: 10 (additional connections allowed)
- **pool_recycle**: 300 seconds (recycle connections after 5 minutes)
- **pool_timeout**: 30 seconds (wait time for connection from pool)

## Session Dependency for FastAPI

### Implementation Pattern
```python
async def get_session() -> AsyncSession:
    async with create_async_session(engine) as session:
        yield session
```

### Usage in Endpoints
```python
@app.get("/tasks")
async def get_tasks(session: AsyncSession = Depends(get_session)):
    # Session automatically closed after request
    pass
```

## Migration Strategy

### Tool: Alembic
- Standard migration framework for SQLAlchemy-based ORMs
- Compatible with SQLModel since SQLModel is built on SQLAlchemy
- Supports forward and rollback operations

### Migration Workflow
1. Update SQLModel models in the code
2. Generate migration script: `alembic revision --autogenerate -m "description"`
3. Review generated migration for accuracy
4. Apply migration: `alembic upgrade head`

### Initial Setup Commands
```bash
# Initialize alembic in project
alembic init alembic

# Configure alembic.ini for async usage
# Set target_metadata to SQLModel.metadata
```

## Neon PostgreSQL Specific Considerations

### Serverless Characteristics
- Connections may be terminated during idle periods
- Need appropriate retry logic for connection failures
- Optimize pool settings for serverless environment

### Connection Efficiency
- Use prepared statements where possible
- Implement proper connection cleanup
- Monitor connection usage patterns

## Error Handling

### Connection Failures
- Implement retry logic with exponential backoff
- Log connection errors for monitoring
- Graceful degradation when database unavailable

### Session Management Errors
- Ensure sessions are always closed even during exceptions
- Implement proper transaction rollback mechanisms
- Log session-related errors for debugging

## Testing Approach

### Test Database
- Use SQLite with aiosqlite for fast, isolated tests
- TEST_DATABASE_URL environment variable for test-specific settings
- Transaction rollback after each test to maintain clean state

### Mocking Strategy
- For unit tests, mock database sessions
- For integration tests, use real database connections
- Implement test fixtures for common data setup

## Security Considerations

### Connection Security
- Use SSL connections to Neon PostgreSQL
- Store database credentials securely in environment variables
- Avoid logging sensitive connection information

### SQL Injection Prevention
- Use parameterized queries through SQLModel/SQLAlchemy
- Validate and sanitize all input before database operations
- Leverage SQLModel's built-in protection against injection

## Performance Optimization

### Query Optimization
- Use appropriate indexes based on access patterns
- Implement pagination for large result sets
- Consider connection pooling for high-throughput scenarios

### Monitoring
- Track connection pool utilization
- Monitor query execution times
- Watch for connection leaks or timeouts