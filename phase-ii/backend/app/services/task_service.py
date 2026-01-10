from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Optional, List
from uuid import UUID
from datetime import datetime
from app.models.task import Task, TaskCreate, TaskUpdate
from app.models.user import User
from sqlalchemy.exc import SQLAlchemyError


class TaskService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_task(self, user_id: UUID, task_data: TaskCreate) -> Task:
        """Create a new task for a user."""
        # Verify user exists (in Phase II Part 1, we just check if user_id is valid)
        # In future phases, we'll add proper authentication

        task = Task(
            title=task_data.title,
            description=task_data.description,
            completed=task_data.completed,
            user_id=user_id
        )

        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)

        return task

    async def get_task(self, task_id: UUID) -> Optional[Task]:
        """Get a specific task by ID."""
        statement = select(Task).where(Task.id == task_id)
        result = await self.session.execute(statement)
        task = result.first()
        return task

    async def get_tasks_for_user(self, user_id: UUID) -> List[Task]:
        """Get all tasks for a specific user."""
        statement = select(Task).where(Task.user_id == user_id)
        result = await self.session.execute(statement)
        tasks = result.all()
        return tasks

    async def update_task(self, task_id: UUID, update_data: TaskUpdate) -> Optional[Task]:
        """Update an existing task."""
        statement = select(Task).where(Task.id == task_id)
        result = await self.session.execute(statement)
        task = result.first()

        if not task:
            return None

        # Update only the fields that are provided
        for field, value in update_data.dict(exclude_unset=True).items():
            if value is not None:
                setattr(task, field, value)

        task.updated_at = datetime.utcnow()

        await self.session.commit()
        await self.session.refresh(task)

        return task

    async def delete_task(self, task_id: UUID) -> bool:
        """Delete a task by ID."""
        statement = select(Task).where(Task.id == task_id)
        result = await self.session.execute(statement)
        task = result.first()

        if not task:
            return False

        await self.session.delete(task)
        await self.session.commit()

        return True

    async def toggle_task_completion(self, task_id: UUID) -> Optional[Task]:
        """Toggle the completion status of a task."""
        statement = select(Task).where(Task.id == task_id)
        result = await self.session.execute(statement)
        task = result.first()

        if not task:
            return None

        task.completed = not task.completed
        task.updated_at = datetime.utcnow()

        await self.session.commit()
        await self.session.refresh(task)

        return task