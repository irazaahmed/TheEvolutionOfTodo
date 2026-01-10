from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List
from app.models.task import Task as TaskModel, TaskCreate, TaskUpdate
from app.schemas.task import TaskResponse
from app.services.task_service import TaskService
from app.api.deps import get_db_session
from sqlmodel.ext.asyncio.session import AsyncSession


router = APIRouter()


@router.get("/users/{user_id}/tasks", response_model=List[TaskResponse])
async def list_tasks(
    user_id: UUID,
    db_session: AsyncSession = Depends(get_db_session)
):
    """Get all tasks for a specific user."""
    service = TaskService(db_session)
    tasks = await service.get_tasks_for_user(user_id)
    return tasks


@router.post("/users/{user_id}/tasks", response_model=TaskResponse, status_code=201)
async def create_task(
    user_id: UUID,
    task_create: TaskCreate,
    db_session: AsyncSession = Depends(get_db_session)
):
    """Create a new task for a user."""
    service = TaskService(db_session)
    task = await service.create_task(user_id, task_create)
    return task


@router.get("/users/{user_id}/tasks/{task_id}", response_model=TaskResponse)
async def get_task(
    user_id: UUID,
    task_id: UUID,
    db_session: AsyncSession = Depends(get_db_session)
):
    """Get a specific task by ID."""
    service = TaskService(db_session)
    task = await service.get_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Verify that the task belongs to the specified user
    if task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/users/{user_id}/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    user_id: UUID,
    task_id: UUID,
    task_update: TaskUpdate,
    db_session: AsyncSession = Depends(get_db_session)
):
    """Update an existing task."""
    service = TaskService(db_session)
    task = await service.get_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Verify that the task belongs to the specified user
    if task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = await service.update_task(task_id, task_update)

    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return updated_task


@router.delete("/users/{user_id}/tasks/{task_id}", status_code=204)
async def delete_task(
    user_id: UUID,
    task_id: UUID,
    db_session: AsyncSession = Depends(get_db_session)
):
    """Delete a task."""
    service = TaskService(db_session)
    task = await service.get_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Verify that the task belongs to the specified user
    if task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")

    success = await service.delete_task(task_id)

    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

    return


@router.patch("/users/{user_id}/tasks/{task_id}/toggle", response_model=TaskResponse)
async def toggle_task_completion(
    user_id: UUID,
    task_id: UUID,
    db_session: AsyncSession = Depends(get_db_session)
):
    """Toggle the completion status of a task."""
    service = TaskService(db_session)
    task = await service.get_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Verify that the task belongs to the specified user
    if task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")

    toggled_task = await service.toggle_task_completion(task_id)

    if not toggled_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return toggled_task