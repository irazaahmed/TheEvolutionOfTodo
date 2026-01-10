# Data Model: Phase I

The system manages a single volatile state representing the todo list.

## Entities

### Task
Represents a single item in the todo list.

| Attribute | Type | Description | Validation |
|-----------|------|-------------|------------|
| `id` | Integer | Sequential unique identifier | Must be > 0 |
| `description` | String | User text describing the task | Cannot be empty or whitespace |
| `is_completed` | Boolean | Whether the task is done | Defaults to `False` |

## State Management

- **Container**: `List[Task]`
- **Scope**: Singleton service within the application process.
- **Lifecycle**: Initialized as an empty list on start; discarded on exit.

## Transitions

- **Add**: Appends a new Task object with a generated ID.
- **Toggle**: Finds Task by ID and flips `is_completed` boolean.
- **Delete**: Removes Task from the list by ID.
- **List**: Returns all tasks currently in the container.
