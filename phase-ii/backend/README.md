# Todo Backend - Phase II Part 1

This is the backend implementation for the Todo application, part of Phase II of "The Evolution of Todo" project. This phase focuses on creating a full-stack web application with persistent storage using FastAPI, SQLModel, and Neon Serverless PostgreSQL.

## Overview

The backend provides REST API endpoints for managing todo tasks with persistent storage. It includes:
- FastAPI application with proper routing
- SQLModel for database modeling
- Neon PostgreSQL for persistent storage
- Complete CRUD operations for todo tasks
- User ownership modeling (without authentication enforcement in this phase)

## Technology Stack

- **Framework**: FastAPI
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Database Driver**: asyncpg

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```bash
   cp .env .env.local
   # Edit .env.local with your database configuration
   ```

4. Start the application:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

## API Endpoints

- `GET /users/{user_id}/tasks` - List all tasks for a user
- `POST /users/{user_id}/tasks` - Create a new task
- `GET /users/{user_id}/tasks/{task_id}` - Get a specific task
- `PUT /users/{user_id}/tasks/{task_id}` - Update a task
- `DELETE /users/{user_id}/tasks/{task_id}` - Delete a task
- `PATCH /users/{user_id}/tasks/{task_id}/toggle` - Toggle task completion status

## Development

This project follows a spec-driven development approach. All functionality is based on the specifications in the `specs/` directory.