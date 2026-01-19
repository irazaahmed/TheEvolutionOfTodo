# Skill: Write Specification

## Purpose
This skill is responsible for creating clear, structured, and phase-scoped specifications using spec-driven development principles.

It converts a feature idea into a deterministic markdown specification that can be safely used for code generation.

## When to Use
Use this skill whenever a new feature, capability, or phase requirement needs to be defined before implementation.

## Inputs
- Current hackathon phase
- Feature name
- Feature description or goal
- Relevant constraints from the Constitution

## Procedure
1. Identify the active hackathon phase and its boundaries.
2. Clearly define the feature purpose.
3. Write user stories in plain, testable language.
4. Define acceptance criteria as explicit conditions.
5. Avoid all implementation or technology-specific details.
6. Ensure the spec can be read and executed by an AI system.

## Output
A markdown specification file containing:
- Feature overview
- User stories
- Acceptance criteria
- Phase constraints

## Quality Rules
- The spec must be phase-limited.
- The spec must be deterministic and unambiguous.
- The spec must not include code or architecture decisions.
