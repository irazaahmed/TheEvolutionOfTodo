# Tasks: Phase I - In-Memory Console Todo Application

**Input**: Design documents from `/specs/001-phase-1-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Path conventions follow the `src/` root structure defined in `plan.md`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure (`src/app/models/`, `src/app/services/`, `src/app/cli/`, `tests/unit/`, `tests/integration/`) per implementation plan
- [X] T002 Initialize Python environment and create `requirements.txt` with `pytest`
- [X] T003 [P] Configure `.gitignore` to exclude `__pycache__`, `.pytest_cache`, and virtual environments

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [X] T004 Create base `Task` data class in `src/app/models/task.py` with `id`, `description`, and `is_done`
- [X] T005 Setup `TodoService` class container in `src/app/services/todo_service.py` with dictionary-based storage and ID counter
- [X] T006 Implement menu-driven UI loop and selection routing in `src/app/cli/router.py`
- [X] T007 Create application entry point in `src/main.py` that handles the initialization and main loop

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Menu-Driven Task Creation (Priority: P1) 🎯 MVP

**Goal**: Allow users to add tasks via Option 1 of the menu.

**Independent Test**: Use Menu Option 1, enter "Buy Milk", then verify it is stored with ID 1.

### Implementation for User Story 1

- [X] T008 [US1] Implement `add_task` in `TodoService` (auto-increment ID)
- [X] T009 [US1] Implement Option 1 handler in `router.py` (Prompt for desc)
- [X] T010 [US1] Add input validation for task descriptions
- [X] T011 [P] [US1] Create unit test for task creation with ID tracking

---

## Phase 4: User Story 2 - Viewing and Managing Tasks (Priority: P2)

**Goal**: Implement Menu Options 2, 3, and 4.

**Independent Test**: Use Menu Option 2 to see list; Option 4 to mark ID 1 as done; Option 3 to update description of ID 1.

### Implementation for User Story 2

- [X] T012 [US2] Implement `get_all_tasks` and `update_task` in `TodoService`
- [X] T013 [US2] Implement `mark_task_done` in `TodoService`
- [X] T014 [US2] Implement Option 2 (View) with formatted ID/Status output
- [X] T015 [US2] Implement Options 3 (Update) and 4 (Done) with ID prompts
- [X] T016 [P] [US2] Create unit tests for updating and completing by numeric ID

---

## Phase 5: User Story 3 - Removing Tasks & Exit (Priority: P3)

**Goal**: Implement Menu Options 5 and 6.

### Implementation for User Story 3

- [X] T017 [US3] Implement `delete_task(task_id)` logic in `TodoService`
- [X] T018 [US3] Implement Option 5 handler in `router.py`
- [X] T019 [US3] Implement Option 6 (Exit) logic
- [X] T020 [P] [US3] Create unit test for deletion and ID validation logic

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final verification and user experience improvements

- [X] T020 Implement "Exit" command to cleanly terminate in `src/app/cli/router.py`
- [X] T021 Add error handling for invalid IDs and unknown commands in `src/app/cli/router.py`
- [X] T022 [P] Create integration tests for end-to-end CLI flows in `tests/integration/test_cli_flows.py`
- [X] T023 Final validation against `quickstart.md` and Phase I Specification

---

## Dependencies & Execution Order

### Phase Dependencies

1. **Setup (Phase 1)**: Must be first.
2. **Foundational (Phase 2)**: Depends on T001-T003.
3. **User Stories (Phase 3-5)**: All depend on Foundational (Phase 2). Should be completed P1 -> P2 -> P3.
4. **Polish (Phase 6)**: Final step.

### Parallel Opportunities

- T003 (gitignore) can be done with T002.
- T011, T016, T019 (Unit tests) can be written in parallel with their respective service logic if using different files, though usually they follow the logic.
- T022 (Integration tests) can be drafted once the router structure (T006) is established.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Setup structure and Foundation.
2. Implement US1 (Add task).
3. **Verify**: Ensure tasks are added correctly in memory.

### Incremental Delivery

1. Foundation ready.
2. Add US1 -> Test.
3. Add US2 -> Test.
4. Add US3 -> Test.
5. Apply Polish.
