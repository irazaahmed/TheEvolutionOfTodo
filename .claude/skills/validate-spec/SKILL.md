# Skill: Validate Specification

## Purpose
This skill validates a specification against the Constitution and phase boundaries to ensure it is safe for implementation.

## When to Use
Use this skill immediately after a specification is written and before any code generation occurs.

## Inputs
- Specification markdown file
- Active hackathon phase
- Constitution rules

## Procedure
1. Check that the spec belongs to the active phase.
2. Detect any future-phase feature leakage.
3. Ensure acceptance criteria are clear and testable.
4. Verify no implementation details are present.
5. Confirm alignment with constitutional rules.

## Output
One of the following:
- Approval to proceed
- A list of required corrections

## Quality Rules
- Validation must be strict.
- Any ambiguity must be flagged.
- No assumptions may be allowed.
