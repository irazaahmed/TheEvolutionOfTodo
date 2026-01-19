---
name: backend-skill
description: Design and implement backend services including API routes, request and response handling, and database connectivity. Use for building and maintaining RESTful backends.
---

# Backend Skill – Routes, Requests, and Database Integration

## Instructions

1. **Route Design**
   - Define clear, RESTful API endpoints
   - Use consistent URL naming conventions
   - Align routes with business entities and actions
   - Group related routes logically

2. **Request Handling**
   - Validate incoming request data strictly
   - Handle query parameters, path variables, and request bodies correctly
   - Reject malformed or unauthorized requests early
   - Avoid leaking internal errors or stack traces

3. **Response Handling**
   - Return predictable and consistent response shapes
   - Use appropriate HTTP status codes
   - Provide meaningful, non-sensitive error messages
   - Ensure response schemas match documented contracts

4. **Database Connectivity**
   - Connect to the database using safe, managed connections
   - Use ORM or query builders consistently
   - Prevent SQL injection with parameterized queries
   - Manage transactions for multi-step operations

5. **Integration Discipline**
   - Keep business logic separate from routing logic
   - Coordinate database access with schema and migration rules
   - Integrate authentication and authorization where required

## Best Practices

- Treat API contracts as stable interfaces
- Validate all external inputs
- Handle errors centrally and consistently
- Avoid tight coupling between routes and database schemas
- Log backend errors safely without exposing sensitive data
- Design routes to be extensible and maintainable

## Example Structure (Conceptual)

```text
GET /tasks
→ Validate auth
→ Fetch tasks from database
→ Return list of tasks

POST /tasks
→ Validate request body
→ Insert new task into database
→ Return created task
