from fastapi import APIRouter, Depends, HTTPException, Path
from uuid import UUID
from typing import List
from app.models.task import Task as TaskModel, TaskCreate, TaskUpdate
from app.schemas.task import TaskResponse
from app.services.task_service import TaskService
from app.api.deps import get_db_session
from app.auth.dependencies import get_current_user_id
from sqlmodel.ext.asyncio.session import AsyncSession


router = APIRouter()


@router.get("/{user_id}/tasks", response_model=List[TaskResponse])
async def list_tasks(
    user_id: UUID,
    current_user_id: UUID = Depends(get_current_user_id),
    db_session: AsyncSession = Depends(get_db_session)
):
    """Get all tasks for the specified user. User must be authenticated as the same user."""
    # Verify that the authenticated user is accessing their own data
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Access denied: Cannot access another user's tasks")

    service = TaskService(db_session)
    tasks = await service.get_tasks_for_user(user_id)
    return tasks


@router.post("/{user_id}/tasks", response_model=TaskResponse, status_code=201)
async def create_task(
    user_id: UUID,
    task_create: TaskCreate,
    current_user_id: UUID = Depends(get_current_user_id),
    db_session: AsyncSession = Depends(get_db_session)
):
    """Create a new task for the specified user. User must be authenticated as the same user."""
    # Verify that the authenticated user is the same as the user in the path
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Access denied: Cannot create tasks for another user")

    service = TaskService(db_session)
    task = await service.create_task(user_id, task_create)
    return task


@router.get("/{user_id}/tasks/{task_id}", response_model=TaskResponse)
async def get_task(
    user_id: UUID,
    task_id: UUID,
    current_user_id: UUID = Depends(get_current_user_id),
    db_session: AsyncSession = Depends(get_db_session)
):
    """Get a specific task by ID for the specified user. User must be authenticated as the same user."""
    # Verify that the authenticated user is accessing their own data
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Access denied: Cannot access another user's tasks")

    service = TaskService(db_session)
    task = await service.get_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Verify that the task belongs to the specified user
    if task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/{user_id}/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    user_id: UUID,
    task_id: UUID,
    task_update: TaskUpdate,
    current_user_id: UUID = Depends(get_current_user_id),
    db_session: AsyncSession = Depends(get_db_session)
):
    """Update an existing task for the specified user. User must be authenticated as the same user."""
    # Verify that the authenticated user is modifying their own data
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Access denied: Cannot modify another user's tasks")

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


@router.delete("/{user_id}/tasks/{task_id}", status_code=204)
async def delete_task(
    user_id: UUID,
    task_id: UUID,
    current_user_id: UUID = Depends(get_current_user_id),
    db_session: AsyncSession = Depends(get_db_session)
):
    """Delete a task for the specified user. User must be authenticated as the same user."""
    # Verify that the authenticated user is deleting their own data
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Access denied: Cannot delete another user's tasks")

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


@router.patch("/{user_id}/tasks/{task_id}/complete", response_model=TaskResponse)
async def toggle_task_completion(
    user_id: UUID,
    task_id: UUID,
    current_user_id: UUID = Depends(get_current_user_id),
    db_session: AsyncSession = Depends(get_db_session)
):
    """Toggle the completion status of a task for the specified user. User must be authenticated as the same user."""
    # Verify that the authenticated user is modifying their own data
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="Access denied: Cannot modify another user's tasks")

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