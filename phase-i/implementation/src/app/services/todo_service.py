from typing import Dict, List, Optional
from src.app.models.task import Task

class TodoService:
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._id_counter = 1

    def add_task(self, description: str) -> Task:
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        task = Task(id=self._id_counter, description=description.strip())
        self._tasks[self._id_counter] = task
        self._id_counter += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        return list(self._tasks.values())

    def update_task(self, task_id: int, new_description: str) -> Optional[Task]:
        if task_id not in self._tasks:
            return None
        if not new_description or not new_description.strip():
            raise ValueError("New description cannot be empty")

        task = self._tasks[task_id]
        task.description = new_description.strip()
        return task

    def mark_task_done(self, task_id: int) -> Optional[Task]:
        if task_id not in self._tasks:
            return None

        task = self._tasks[task_id]
        task.is_done = True
        return task

    def delete_task(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
