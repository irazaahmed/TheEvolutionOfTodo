from dataclasses import dataclass

@dataclass
class Task:
    id: int
    description: str
    is_done: bool = False

    def __str__(self):
        status = "[X]" if self.is_done else "[ ]"
        return f"{self.id}. {status} {self.description}"
