import pytest
from src.app.services.todo_service import TodoService

def test_add_task_numeric_ids():
    service = TodoService()
    task1 = service.add_task("First")
    task2 = service.add_task("Second")
    assert task1.id == 1
    assert task2.id == 2
    assert task1.description == "First"

def test_delete_task():
    service = TodoService()
    task = service.add_task("To delete")
    assert service.delete_task(1) is True
    assert len(service.get_all_tasks()) == 0

def test_mark_done():
    service = TodoService()
    task = service.add_task("Pending")
    updated = service.mark_task_done(1)
    assert updated.is_done is True
