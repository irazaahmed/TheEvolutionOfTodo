---
id: 001
title: Establish The Evolution of Todo Constitution
stage: constitution
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: default
command: /sp.constitution
labels: [architecture, SDD, constitution]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

You are an AI system architect and constitution author.

Write a comprehensive Constitution for a project named "The Evolution of Todo", built for Hackathon II using Spec-Driven Development, Claude CLI, Spec-Kit Plus, reusable agents, and reusable skills.

This Constitution will govern the entire project across all phases and must be written in clear, structured Markdown.

The Constitution must include the following sections in detail:

1. Purpose and Vision
Explain that this project represents the evolution of a single product from a simple console application to a cloud-native, AI-powered, event-driven system. Emphasize AI-first, spec-driven development and reusable intelligence.

2. Core Principles
Define non-negotiable principles such as:
- Spec-Driven Development only
- No manual coding
- Evolution over duplication
- AI as system builder, human as architect
- Deterministic, auditable outputs
- Phase isolation and discipline

3. Phase Governance Rules
Clearly define rules for all five phases:
- Phase I: In-memory Python console app
- Phase II: Full-stack web application
- Phase III: AI chatbot with MCP tools
- Phase IV: Local Kubernetes deployment
- Phase V: Cloud-native, event-driven system

State that no future-phase features may appear early and each phase must build on the previous one.

4. Specification Rules
Define how specifications must be written, validated, evolved, and stored.
Mention that:
- All functionality must originate from specs
- Specs must precede code
- Incorrect behavior requires spec refinement, not code patches

5. Agent Architecture
Describe the role of reusable agents in the system.
Explicitly mention agents such as:
- main-orchestrator
- constitution-guardian
- spec-author
- implementation agents
- evolution-manager
- repository-governance agents

Define what agents are allowed and forbidden to do.

6. Reusable Skills Architecture
Describe reusable skills as procedural intelligence.
Mention skills such as:
- write-spec
- validate-spec
- generate-code
- refactor-for-next-phase
- repo-hygiene
- phase-planning

Clarify the difference between agents (decision-makers) and skills (repeatable workflows).

7. Execution Flow
Define the mandatory workflow:
- Constitution → Phase identification → Spec writing → Spec validation → Code generation → Validation → Evolution

State that skipping steps is forbidden.

8. Repository and Structure Rules
Define strict rules for:
- Phase-based folder isolation
- No duplication across phases
- Clear, auditable structure

9. Error Handling and Corrections
Explain that all errors must be resolved by refining specs, agents, or skills, never by manual fixes.

10. Compliance and Enforcement
State that any violation of this Constitution invalidates the work.
Define that agents must enforce this Constitution at all times.

11. Living Document Clause
Clarify that this Constitution may evolve, but only through explicit, intentional updates, never silently.

Tone:
- Authoritative
- Architectural
- Clear and enforceable
- Suitable for judges and auditors

Output only the final Constitution in well-structured Markdown.

## Response snapshot

I have generated and finalized the comprehensive Constitution for "The Evolution of Todo".
The document establishes 6 core principles (Spec-Driven Only, No Manual Coding, etc.), defines the 5-phase evolution model, and sets strict rules for agent and skill architecture.
It is stored at `.specify/memory/constitution.md` and versioned as 1.0.0.

## Outcome

- ✅ Impact: Project principles established; SDD mandate enforced.
- 🧪 Tests: none (Review process only)
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: /sp.specify for Phase I
- 🧠 Reflection: The transition from a template to a concrete constitution was successful.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Implement Phase I specification.
