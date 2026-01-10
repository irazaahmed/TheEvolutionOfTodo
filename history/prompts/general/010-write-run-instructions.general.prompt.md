---
id: 10
title: Write Phase I run instructions
stage: general
date_iso: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: anonymous
command: Write clear, step-by-step instructions to run the Phase I Todo console application
labels: ["documentation", "instructions", "phase-1"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - history/prompts/general/010-write-run-instructions.general.prompt.md
tests_yaml:
  - none
---

# Prompt
Write clear, step-by-step instructions to run the Phase I Todo console application from the command line.

Assumptions:
- Python is installed
- The user is in the repository root

Instructions must include:
- Navigating to the correct directory
- Installing dependencies (if required)
- Running the application
- Running tests (if applicable)

Output should be suitable for inclusion in README.md.

# Response
To run the Phase I Todo console application, follow these steps:

### Phase I: In-Memory Console Application

#### 1. Navigate to the Implementation Directory
All Phase I implementation files are isolated within the `phase-1/` directory. From the repository root, run:
```bash
cd phase-1/implementation
```

#### 2. Install Dependencies
Phase I uses only the Python Standard Library for the application logic, but requires `pytest` for running the test suite. Install it using the provided `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### 3. Run the Application
Start the interactive Todo console application by executing the main entry point:
```bash
python src/main.py
```
*Note: You can type `help` within the application to see all available commands (add, list, done, delete).*

#### 4. Run Tests
To verify the implementation logic and CLI routing, run the test suite from the `phase-1/implementation` directory:
```bash
python -m pytest tests/ -v
```
