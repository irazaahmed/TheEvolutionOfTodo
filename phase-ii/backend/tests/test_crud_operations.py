import pytest
import asyncio
from httpx import AsyncClient
from uuid import uuid4
from app.main import app
from sqlmodel import select
from app.models.task import Task
from app.core.database import async_engine, get_async_session
from app.services.task_service import TaskService
from sqlmodel.ext.asyncio.session import AsyncSession


@pytest.mark.asyncio
async def test_full_crud_operations():
    """Test all CRUD operations with Neon PostgreSQL persistence"""
    async with AsyncClient(app=app, base_url="http://test") as ac:

        # Generate a user ID for testing
        user_id = uuid4()

        # Test: Create a task
        create_response = await ac.post(
            f"/api/v1/users/{user_id}/tasks",
            json={"title": "Test Task", "description": "Test Description"}
        )
        assert create_response.status_code == 201

        created_task = create_response.json()
        task_id = created_task['id']
        assert created_task['title'] == "Test Task"
        assert created_task['description'] == "Test Description"
        assert created_task['completed'] is False

        # Test: Get the created task
        get_response = await ac.get(f"/api/v1/users/{user_id}/tasks/{task_id}")
        assert get_response.status_code == 200

        retrieved_task = get_response.json()
        assert retrieved_task['id'] == task_id
        assert retrieved_task['title'] == "Test Task"

        # Test: List tasks for the user
        list_response = await ac.get(f"/api/v1/users/{user_id}/tasks")
        assert list_response.status_code == 200

        tasks_list = list_response.json()
        assert len(tasks_list) == 1
        assert tasks_list[0]['id'] == task_id

        # Test: Update the task
        update_response = await ac.put(
            f"/api/v1/users/{user_id}/tasks/{task_id}",
            json={"title": "Updated Task", "description": "Updated Description", "completed": True}
        )
        assert update_response.status_code == 200

        updated_task = update_response.json()
        assert updated_task['title'] == "Updated Task"
        assert updated_task['completed'] is True

        # Test: Toggle task completion
        toggle_response = await ac.patch(f"/api/v1/users/{user_id}/tasks/{task_id}/toggle")
        assert toggle_response.status_code == 200

        toggled_task = toggle_response.json()
        assert toggled_task['completed'] is False  # Should be toggled back to False

        # Test: Delete the task
        delete_response = await ac.delete(f"/api/v1/users/{user_id}/tasks/{task_id}")
        assert delete_response.status_code == 204

        # Verify task is deleted by trying to retrieve it
        get_deleted_response = await ac.get(f"/api/v1/users/{user_id}/tasks/{task_id}")
        assert get_deleted_response.status_code == 404


@pytest.mark.asyncio
async def test_error_responses():
    """Test error responses for invalid inputs and non-existent resources"""
    async with AsyncClient(app=app, base_url="http://test") as ac:

        user_id = uuid4()
        fake_task_id = uuid4()

        # Test: Create task with invalid data (missing title)
        create_invalid_response = await ac.post(
            f"/api/v1/users/{user_id}/tasks",
            json={"description": "Test Description"}  # Missing required title
        )
        assert create_invalid_response.status_code == 422  # Validation error

        # Test: Get non-existent task
        get_nonexistent_response = await ac.get(f"/api/v1/users/{user_id}/tasks/{fake_task_id}")
        assert get_nonexistent_response.status_code == 404


if __name__ == "__main__":
    pytest.main([__file__])