# Quickstart: Phase I

Phase I is a standalone console application. No external services or databases are required.

## Prerequisites
- Python 3.11+
- terminal/console access

## Running the Application
To start the interactive session:
```bash
python src/main.py
```

## Available Commands
Once running, the application will prompt for input:
- `add "description"`: Create a new task (use quotes for multi-word descriptions)
- `list` or `ls`: Show all tasks
- `done <id>`: Toggle completion status (use task number or ID)
- `delete <id>`: Remove a task (use task number or ID)
- `help`: Show available commands
- `exit` or `quit`: Terminate the session (Clears all data)

## Testing
Run the test suite using pytest:
```bash
pytest
```
