class TaskNotFoundError(Exception):
    """Raised when a task operation is attempted on a non-existent task"""
    def __init__(self, task_id):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found")


class ValidationError(Exception):
    """Raised when input validation fails"""
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(message)


class DatabaseError(Exception):
    """Raised when database operations fail"""
    def __init__(self, message, original_exception=None):
        self.message = message
        self.original_exception = original_exception
        super().__init__(message)