# Service Layer Architecture: Todo Backend

**Feature**: 1-backend-core
**Created**: 2026-01-09
**Status**: Design

## Overview

The service layer encapsulates all business logic for the Todo application, separating it from API concerns and database operations. This layer handles validation, business rules, and orchestrates database operations.

## Service Components

### 1. TaskService

#### Responsibilities
- Manage all task-related operations
- Handle input validation and transformation
- Coordinate database transactions
- Apply business rules and constraints

#### Methods

**create_task(user_id: UUID, title: str, description: Optional[str]) -> Task**
- Validates input parameters
- Creates new task with default values (completed=False)
- Saves to database
- Returns created Task object

**get_task(task_id: UUID) -> Optional[Task]**
- Retrieves task by ID
- Returns None if not found

**get_tasks_for_user(user_id: UUID) -> List[Task]**
- Retrieves all tasks for a specific user
- Returns empty list if none found

**update_task(task_id: UUID, update_data: TaskUpdate) -> Optional[Task]**
- Updates task with provided data
- Validates update parameters
- Returns updated task or None if not found

**delete_task(task_id: UUID) -> bool**
- Deletes task by ID
- Returns True if successful, False if not found

**toggle_task_completion(task_id: UUID) -> Optional[Task]**
- Toggles the completion status of a task
- Updates the updated_at timestamp
- Returns updated task or None if not found

#### Validation Logic
- Title must be between 1-255 characters
- Description must be 1000 characters or less
- user_id must reference an existing user (in future phases with auth enforcement)

### 2. UserService

#### Responsibilities
- Manage user-related operations
- Handle user creation and retrieval
- Prepare user data for association with tasks

#### Methods

**create_user() -> User**
- Creates a new user with default values
- Saves to database
- Returns created User object

**get_user(user_id: UUID) -> Optional[User]**
- Retrieves user by ID
- Returns None if not found

## Error Handling Strategy

### Custom Exceptions
- `TaskNotFoundError`: Raised when a task operation is attempted on a non-existent task
- `UserNotFoundError`: Raised when a user operation is attempted on a non-existent user
- `ValidationError`: Raised when input validation fails
- `DatabaseError`: Raised when database operations fail

### Transaction Management
- Each service method manages its own database transaction
- Automatic rollback on exceptions
- Proper session cleanup after operations

## Data Transformation

### Input Transformation
- Convert API request objects to database models
- Apply default values where needed
- Validate data types and constraints

### Output Transformation
- Convert database models to API response objects
- Format timestamps consistently
- Exclude sensitive information

## Future Extensibility

### Authentication Placeholder
- Service methods accept user identifiers without validation (for Phase II Part 1)
- Will be enhanced with authentication validation in Phase II Part 2
- Interface remains consistent to prevent breaking changes

### Audit Trail
- Timestamps captured for all operations
- Ready for audit logging implementation in future phases

## Dependencies

- SQLModel for database operations
- Pydantic for data validation
- FastAPI dependency injection system
- Database session management utilities