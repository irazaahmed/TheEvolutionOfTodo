<!--
Sync Impact Report:
- Version change: [CONSTITUTION_VERSION] -> 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] -> I. Spec-Driven Development Only
  - [PRINCIPLE_2_NAME] -> II. Manual Code Writing Forbidden
  - [PRINCIPLE_3_NAME] -> III. Evolution Over Duplication
  - [PRINCIPLE_4_NAME] -> IV. AI as Builder, Human as Architect
  - [PRINCIPLE_5_NAME] -> V. Phase Isolation and Discipline
  - [PRINCIPLE_6_NAME] -> VI. Deterministic, Auditable Outputs
- Added sections:
  - Phase Governance Rules
  - Specification Rules
  - Agent Architecture
  - Reusable Skills Architecture
  - Execution Flow
  - Repository and Structure Rules
  - Error Handling and Corrections
  - Compliance and Enforcement
  - Living Document Clause
- Removed sections: None
- Templates requiring updates:
  - ✅ updated: .specify/memory/constitution.md
  - ⚠ pending: .specify/templates/plan-template.md
  - ⚠ pending: .specify/templates/spec-template.md
  - ⚠ pending: .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->

# The Evolution of Todo Constitution

## Purpose and Vision
This project represents the evolution of a single Todo product from a simple console application to a cloud-native, AI-powered, event-driven system. The primary objective is to demonstrate AI-first, spec-driven development (SDD) using reusable intelligence and structured workflows. Every step of development is handled by AI agents guided by rigorous specifications and architectural documentation.

## Core Principles

### I. Spec-Driven Development Only
All functionality, logic, and behavior MUST originate from formal specifications. No code may be written or modified without a corresponding update to the specification and implementation plan. Specifications are the authoritative source of truth.

### II. Manual Code Writing Forbidden
Manual editing of source code by humans is strictly prohibited. AI agents must generate all code based on validated specifications. If a code output is incorrect, the agent must refine the specification or the implementation plan, never patch the code directly.

### III. Evolution Over Duplication
The codebase must evolve incrementally. Code from previous phases should be transitioned, refactored, or migrated to the new stack rather than being duplicated. Redundancy across phase boundaries is a failure of architecture.

### IV. AI as Builder, Human as Architect
The AI serves as the primary system builder, executing tasks and generating artifacts. The human user acts as the high-level architect, providing vision, clarifying requirements, and approving major architectural decisions.

### V. Phase Isolation and Discipline
The project follows a strict five-phase model. Features, libraries, or architectural patterns reserved for future phases MUST NOT be introduced early. Phase boundaries are non-negotiable gates that ensure sustainable growth.

### VI. Deterministic, Auditable Outputs
The development process must be auditable. Every prompt, decision, and code change must be recorded in Prompt History Records (PHRs) and Architecture Decision Records (ADRs). Outputs must be as deterministic as possible through rigorous spec validation.

## Phase Governance Rules
The project evolves through five distinct phases:
- **Phase I**: In-memory Python console application. Focus on basic logic and local state.
- **Phase II**: Full-stack web application. Focus on UI/UX, persistence, and API design.
- **Phase III**: AI chatbot with MCP tools. Focus on LLM integration and tool-use.
- **Phase IV**: Local Kubernetes deployment. Focus on containerization and orchestration.
- **Phase V**: Cloud-native, event-driven system. Focus on scalability and asynchronous patterns.

Each phase must be completed and validated before transitioning. No future-phase tech (e.g., Kubernetes in Phase I) is allowed.

## Specification Rules
- **Precedence**: Specs MUST precede code. No "reverse-specing" of existing code.
- **Validation**: Specs must be validated by dedicated agents for completeness, consistency, and feasibility.
- **Refinement**: Incorrect system behavior is treated as a bug in the specification. Fix the spec, then regenerate the code.
- **Storage**: Specs are stored in `specs/<feature>/spec.md` and are versioned alongside the code.

## Agent Architecture
The system uses a hierarchy of specialized, reusable agents:
- **main-orchestrator**: Identifies project phase, delegates tasks, and enforces governance.
- **constitution-guardian**: Verifies that all actions align with these principles.
- **spec-author**: Drafts requirements, user stories, and acceptance criteria.
- **implementation-agents**: Specialized agents (e.g., python-implementation) that convert plans into code.
- **evolution-manager**: Manages transitions between phases and prevents duplication.
- **repo-governance**: Enforces folder boundaries and repository hygiene.

Agents are forbidden from bypassing spec-driven workflows or making manual code edits without a plan.

## Reusable Skills Architecture
Skills are procedural, repeatable workflows that agents use to execute specific SDD tasks:
- **write-spec**: Standardized drafting of feature requirements.
- **validate-spec**: Multi-perspective review of specifications.
- **generate-code**: The process of translating a plan into functional source code.
- **refactor-for-next-phase**: Mapping existing logic to new technology stacks.
- **repo-hygiene**: Automated cleanup and structural verification.
- **phase-planning**: The architectural workflow for phase transitions.

**Distinction**: Agents are the decision-making entities that use logic and context. Skills are the repeatable, codified procedures they follow.

## Execution Flow
The mandatory workflow for any change is:
1. **Constitution Check**: Ensure the request aligns with project principles.
2. **Phase Identification**: Verify the active phase and boundary constraints.
3. **Spec Writing**: Create or update the `spec.md` with explicit requirements.
4. **Spec Validation**: Verify the spec is implementable and complete.
5. **Plan/Task Generation**: Create `plan.md` and `tasks.md`.
6. **Code Generation**: Trigger implementation agents to generate code.
7. **Validation**: Run tests and verify against acceptance criteria.
8. **Knowledge Capture**: Create a PHR to record the cycle.

Skipping any step in this flow is a violation of the constitution.

## Repository and Structure Rules
- **Isolation**: Each phase has dedicated directories or clear logical separation.
- **No Duplication**: Logic must not be duplicated across phase folders.
- **Auditability**: The `history/` directory must contain a complete record of prompts (PHRs) and decisions (ADRs).
- **Structure**: All artifacts must follow the directory structure defined in `CLAUDE.md`.

## Error Handling and Corrections
All errors (logic bugs, runtime errors, or architectural flaws) must be resolved by:
1. Identifying the failure point in the spec or plan.
2. Updating the spec/plan/task artifact.
3. Redeploying the implementation agent to fix the code.
Manual "quick fixes" in the terminal or code editor are strictly forbidden.

## Compliance and Enforcement
Any output or work produced that violates this Constitution is considered invalid and must be reverted. Agents, specifically the **constitution-guardian**, must verify compliance before any commit or phase transition.

## Living Document Clause
This Constitution is a living document. It may evolve as the project grows into later phases. However, changes must be made through explicit, intentional updates to this file, accompanied by a version bump and an ADR explaining the rationale for the change.

---
**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
