# Data Model: Todo Application Backend

**Feature**: 1-backend-core
**Created**: 2026-01-09
**Status**: Design

## Entity: Todo Task

### Attributes
- **id**: UUID (Primary Key, Auto-generated)
  - Type: uuid.UUID or int (auto-increment)
  - Constraints: Not Null, Unique
  - Description: Unique identifier for each task

- **title**: String
  - Type: str
  - Constraints: Not Null, Max Length 255
  - Description: Brief title of the task

- **description**: String (Optional)
  - Type: str
  - Constraints: Nullable, Max Length 1000
  - Description: Detailed description of the task

- **completed**: Boolean
  - Type: bool
  - Constraints: Not Null, Default False
  - Description: Flag indicating if the task is completed

- **user_id**: UUID (Foreign Key)
  - Type: uuid.UUID or int
  - Constraints: Not Null, Foreign Key Reference to User.id
  - Description: Identifier of the user who owns this task

- **created_at**: DateTime
  - Type: datetime.datetime
  - Constraints: Not Null, Auto-generated
  - Description: Timestamp when the task was created

- **updated_at**: DateTime
  - Type: datetime.datetime
  - Constraints: Not Null, Auto-updating
  - Description: Timestamp when the task was last updated

### Relationships
- **One User** to **Many Tasks** (user_id foreign key)

### Validation Rules
- Title must be provided and not empty
- Title length must be between 1 and 255 characters
- Description length must not exceed 1000 characters
- user_id must reference an existing user
- created_at and updated_at are managed automatically

## Entity: User

### Attributes
- **id**: UUID (Primary Key, Auto-generated)
  - Type: uuid.UUID or int (auto-increment)
  - Constraints: Not Null, Unique
  - Description: Unique identifier for each user

- **created_at**: DateTime
  - Type: datetime.datetime
  - Constraints: Not Null, Auto-generated
  - Description: Timestamp when the user was registered

- **updated_at**: DateTime
  - Type: datetime.datetime
  - Constraints: Not Null, Auto-updating
  - Description: Timestamp when the user record was last updated

### Relationships
- **One User** to **Many Tasks** (as referenced by task.user_id)

### Validation Rules
- created_at and updated_at are managed automatically
- No direct modification of ID allowed

## State Transitions

### Task Completion
- **From**: completed = False
- **To**: completed = True
- **Trigger**: PATCH /users/{user_id}/tasks/{task_id}/toggle endpoint
- **Validation**: Task must exist and belong to the user

### Task Update
- **Action**: PUT /users/{user_id}/tasks/{task_id} endpoint
- **Validation**:
  - Task must exist and belong to the user
  - Updated fields must pass validation rules
  - updated_at field is automatically updated

## Indexes

### Todo Task
- Primary Index: id (automatically created)
- Foreign Key Index: user_id (for efficient user-task lookups)
- Composite Index: (user_id, completed) for efficient filtered queries

### User
- Primary Index: id (automatically created)