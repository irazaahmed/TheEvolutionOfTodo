# Quickstart Guide: Todo Backend

**Feature**: 1-backend-core
**Created**: 2026-01-09
**Status**: Draft

## Overview

This guide provides instructions to set up and run the Todo backend application with FastAPI, SQLModel, and Neon PostgreSQL.

## Prerequisites

- Python 3.8+
- pip package manager
- Access to Neon PostgreSQL account (or local PostgreSQL for development)
- Environment variables configured for database connection

## Setup Instructions

### 1. Clone and Navigate to Project
```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn sqlmodel sqlalchemy asyncpg python-dotenv
```

### 4. Configure Environment Variables
Create a `.env` file in the project root with the following:
```env
DATABASE_URL=postgresql+asyncpg://username:password@host:port/database_name
NEON_DATABASE_URL=<your_neon_database_url>
TEST_DATABASE_URL=sqlite+aiosqlite:///./test.db  # For testing
```

### 5. Initialize Database
```bash
# Run migrations to create the initial schema
python -m alembic upgrade head
```

### 6. Start the Application
```bash
uvicorn main:app --reload --port 8000
```

## API Endpoints

Once running, the API will be available at `http://localhost:8000` with the following endpoints:

- `GET /users/{user_id}/tasks` - List all tasks for a user
- `POST /users/{user_id}/tasks` - Create a new task
- `GET /users/{user_id}/tasks/{task_id}` - Get a specific task
- `PUT /users/{user_id}/tasks/{task_id}` - Update a task
- `DELETE /users/{user_id}/tasks/{task_id}` - Delete a task
- `PATCH /users/{user_id}/tasks/{task_id}/toggle` - Toggle task completion status

## Testing the API

### Create a Task
```bash
curl -X POST "http://localhost:8000/users/123e4567-e89b-12d3-a456-426614174000/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Sample task", "description": "This is a sample task"}'
```

### List Tasks
```bash
curl "http://localhost:8000/users/123e4567-e89b-12d3-a456-426614174000/tasks"
```

## Development

### Running Tests
```bash
pytest
```

### API Documentation
- Interactive documentation available at `http://localhost:8000/docs`
- Alternative JSON schema at `http://localhost:8000/openapi.json`