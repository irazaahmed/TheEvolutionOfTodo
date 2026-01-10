# Research Findings: Phase II Part 1 - Backend Core and Data Layer

**Feature**: 1-backend-core
**Created**: 2026-01-09
**Status**: Completed

## R1.1: Neon PostgreSQL Connection Configuration

### Decision:
Use asyncpg with SQLAlchemy/SQLModel for Neon PostgreSQL connection with connection pooling

### Rationale:
Neon PostgreSQL is a serverless PostgreSQL offering that supports connection pooling and pgBouncer for efficient connection management. The asyncpg driver provides async/await support which integrates well with FastAPI's async nature.

### Alternatives Considered:
- psycopg2: Traditional PostgreSQL driver but less async-friendly
- Sync drivers: Would block FastAPI's async performance benefits
- Direct Neon connection: Would require more manual configuration

## R1.2: SQLModel Schema Design Patterns

### Decision:
Use SQLModel with Pydantic validation for Todo Task schema, following standard patterns for web applications

### Rationale:
SQLModel combines the power of SQLAlchemy and Pydantic, allowing for both database modeling and request/response validation in one class. This reduces code duplication and maintains consistency.

### Alternatives Considered:
- Separate SQLAlchemy and Pydantic models: Creates duplication
- Pure Pydantic models: No database integration
- Pure SQLAlchemy: Less validation features

## R1.3: FastAPI Dependency Injection for DB

### Decision:
Use FastAPI's dependency system with SQLModel's create_session generator for database session management

### Rationale:
This is the recommended pattern in FastAPI documentation for database connections. It ensures proper session lifecycle management and automatic cleanup after requests.

### Alternatives Considered:
- Global database session: Risk of connection leaks
- Manual session management in each endpoint: Repetitive and error-prone
- Middleware-based approach: Less flexible for specific endpoint needs

## R1.4: Migration Strategy with SQLModel

### Decision:
Use Alembic for database migrations with SQLModel's SQLModel.metadata for table reflection

### Rationale:
Alembic is the standard migration tool for SQLAlchemy-based ORMs. SQLModel is built on SQLAlchemy, so Alembic provides the most robust migration capabilities with good Neon PostgreSQL compatibility.

### Alternatives Considered:
- Raw SQL migrations: Not version-controlled or tracked
- Manual schema management: Prone to errors and inconsistency
- Third-party migration tools: Less compatible with SQLModel