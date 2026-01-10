# API Contracts: Frontend Application and Full-Stack Integration

## Authentication API Contracts

### User Registration
```
POST /api/v1/auth/register
Content-Type: application/json
Accept: application/json

Request Body:
{
  "email": "user@example.com",
  "password": "securePassword123"
}

Success Response (200):
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "user_id": "123e4567-e89b-12d3-a456-426614174000"
}

Error Response (400):
{
  "message": "Validation error",
  "code": "VALIDATION_ERROR",
  "details": {
    "errors": [
      {
        "field": "email",
        "message": "Invalid email format",
        "type": "value_error"
      }
    ]
  }
}
```

### User Login
```
POST /api/v1/auth/login
Content-Type: application/json
Accept: application/json

Request Body:
{
  "email": "user@example.com",
  "password": "securePassword123"
}

Success Response (200):
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "user_id": "123e4567-e89b-12d3-a456-426614174000"
}

Error Response (401):
{
  "message": "Incorrect email or password",
  "code": "INVALID_CREDENTIALS",
  "details": null,
  "timestamp": "2026-01-10T10:30:00.000000"
}
```

## Task Management API Contracts

### Get User's Tasks
```
GET /api/v1/tasks
Authorization: Bearer {access_token}
Accept: application/json

Success Response (200):
[
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "title": "Complete project",
    "description": "Finish the todo application",
    "completed": false,
    "user_id": "123e4567-e89b-12d3-a456-426614174000",
    "created_at": "2026-01-10T10:00:00.000000",
    "updated_at": "2026-01-10T10:00:00.000000"
  }
]

Error Response (401/403):
{
  "message": "Unauthorized",
  "code": "HTTP_401",
  "details": null,
  "timestamp": "2026-01-10T10:30:00.000000"
}
```

### Create New Task
```
POST /api/v1/tasks
Authorization: Bearer {access_token}
Content-Type: application/json
Accept: application/json

Request Body:
{
  "title": "New task",
  "description": "Task description (optional)"
}

Success Response (201):
{
  "id": "123e4567-e89b-12d3-a456-426614174001",
  "title": "New task",
  "description": "Task description (optional)",
  "completed": false,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "created_at": "2026-01-10T10:30:00.000000",
  "updated_at": "2026-01-10T10:30:00.000000"
}

Error Response (422):
{
  "message": "Validation error",
  "code": "VALIDATION_ERROR",
  "details": {
    "errors": [
      {
        "field": "title",
        "message": "Field required",
        "type": "missing"
      }
    ]
  }
}
```

### Update Task
```
PUT /api/v1/tasks/{task_id}
Authorization: Bearer {access_token}
Content-Type: application/json
Accept: application/json

Request Body:
{
  "title": "Updated task title",
  "description": "Updated description",
  "completed": false
}

Success Response (200):
{
  "id": "123e4567-e89b-12d3-a456-426614174001",
  "title": "Updated task title",
  "description": "Updated description",
  "completed": false,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "created_at": "2026-01-10T10:30:00.000000",
  "updated_at": "2026-01-10T10:35:00.000000"
}

Error Response (404):
{
  "message": "Task not found",
  "code": "TASK_NOT_FOUND",
  "details": {
    "task_id": "123e4567-e89b-12d3-a456-426614174001"
  },
  "timestamp": "2026-01-10T10:35:00.000000"
}
```

### Toggle Task Completion
```
PATCH /api/v1/tasks/{task_id}/toggle
Authorization: Bearer {access_token}
Accept: application/json

Success Response (200):
{
  "id": "123e4567-e89b-12d3-a456-426614174001",
  "title": "Updated task title",
  "description": "Updated description",
  "completed": true,  // Toggled to opposite state
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "created_at": "2026-01-10T10:30:00.000000",
  "updated_at": "2026-01-10T10:40:00.000000"
}
```

### Delete Task
```
DELETE /api/v1/tasks/{task_id}
Authorization: Bearer {access_token}

Success Response (204): No Content

Error Response (404):
{
  "message": "Task not found",
  "code": "TASK_NOT_FOUND",
  "details": {
    "task_id": "123e4567-e89b-12d3-a456-426614174001"
  },
  "timestamp": "2026-01-10T10:45:00.000000"
}
```