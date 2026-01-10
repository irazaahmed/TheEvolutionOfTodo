---
id: 13
title: Regenerate Phase I implementation for menu-driven UX
stage: green
date_iso: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-phase-1-todo-app
branch: main
user: anonymous
command: /sp.implement
labels: ["implementation", "refactoring", "menu-driven", "cleanup", "phase-1"]
links:
  spec: specs/001-phase-1-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files_yaml:
  - phase-1/implementation/src/app/models/task.py
  - phase-1/implementation/src/app/services/todo_service.py
  - phase-1/implementation/src/app/cli/router.py
  - phase-1/implementation/src/main.py
  - phase-1/implementation/tests/unit/test_todo_service.py
  - phase-1/implementation/requirements.txt
tests_yaml:
  - phase-1/implementation/tests/unit/test_todo_service.py
---

# Prompt
Regenerate Phase I implementation strictly from the updated specs.
Clean the repository by removing all unused or obsolete files.
Deliver a simple, beginner-friendly, and attractive CLI user experience.

UX rules:
1. Welcome to Todo App
2. Numbered menu (1-6)
3. Interaction: Numeric input only
4. Task IDs: Sequential numeric (1, 2, 3...)
5. Storage: In-memory only

# Response
Successfully regenerated the Phase I Todo CLI application with the new menu-driven interaction model.

## Cleanup Summary
- Removed all legacy command-based implementation artifacts (test scripts, debug files, validation experiments).
- Deleted obsolete files at `phase-1/implementation/`.

## New Implementation
- **State Machine**: Re-implemented the CLI as a state-based loop in `src/app/cli/router.py`.
- **Menu System**: Options 1 through 6 cover the complete CRUD lifecycle and application exit.
- **Model Evolution**: Updated `Task` to use simple integer IDs.
- **Service Efficiency**: `TodoService` now uses dictionary-based storage for O(1) task retrieval by ID.
- **Package Hygiene**: Standardized as a Python package to support `python -m src.main` execution.

The resulting codebase is clean, isolated, and strictly follows the Phase I boundaries.
