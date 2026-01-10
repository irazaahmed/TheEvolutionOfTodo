---
name: database-skill
description: Design and manage relational databases including schema design, table creation, and controlled migrations. Use for PostgreSQL and serverless databases like Neon.
---

# Database Skill – Schema Design & Migrations

## Instructions

1. **Schema Design**
   - Identify entities and relationships clearly
   - Use appropriate data types for each field
   - Define primary keys, foreign keys, and constraints
   - Normalize data where appropriate, avoid unnecessary duplication
   - Plan for future extensibility

2. **Table Creation**
   - Create tables with explicit columns and constraints
   - Enforce NOT NULL, UNIQUE, and CHECK constraints where required
   - Use indexes thoughtfully for frequently queried fields
   - Avoid premature optimization but prevent obvious inefficiencies

3. **Migrations**
   - Use migration files or tools for all schema changes
   - Ensure migrations are repeatable and reversible when possible
   - Never modify production schemas manually
   - Version migrations clearly and apply them in order
   - Test migrations on non-production environments first

4. **Data Integrity**
   - Use foreign key constraints to enforce relationships
   - Wrap multi-step operations in transactions
   - Protect against orphaned or inconsistent records

5. **Environment Awareness**
   - Account for serverless database behavior (e.g., Neon)
   - Design schemas that work reliably across cold starts
   - Keep connection usage efficient and predictable

## Best Practices

- Treat the database schema as a long-term contract
- Prefer explicit constraints over relying on application logic
- Keep migrations small and focused
- Document schema decisions that impact multiple services
- Coordinate schema changes with backend and auth logic
- Regularly review indexes and query patterns

## Example Structure (Conceptual)

```text
User Table
- id (primary key)
- email (unique, indexed)
- password_hash
- created_at

Task Table
- id (primary key)
- user_id (foreign key → users.id)
- title
- completed
- created_at
