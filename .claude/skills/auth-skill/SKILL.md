---
name: auth-skill
description: Design and implement secure authentication systems including signup, signin, password hashing, JWT tokens, and Better Auth integration.
---

# Auth Skill – Secure Authentication & Authorization

## Instructions

1. **Signup Flow**
   - Validate user input strictly (email, password, required fields)
   - Hash passwords securely before storage
   - Prevent duplicate accounts
   - Return clear, non-sensitive error messages

2. **Signin Flow**
   - Verify credentials securely
   - Never expose whether email or password was incorrect
   - Apply rate-limiting awareness to prevent brute force attacks
   - Issue tokens only after successful verification

3. **Password Hashing**
   - Use strong, industry-standard hashing algorithms
   - Always hash passwords on the backend
   - Never store or log plaintext passwords
   - Support future hash upgrades if needed

4. **JWT Token Handling**
   - Generate signed JWT access tokens
   - Define clear expiration policies
   - Validate tokens on every protected request
   - Handle token expiration and invalidation safely
   - Support logout and session cleanup

5. **Better Auth Integration**
   - Use Better Auth only in the backend layer
   - Configure trusted origins and callbacks safely
   - Avoid open redirects and misconfigured callbacks
   - Ensure Better Auth does not leak into frontend dependencies

## Best Practices

- Separate authentication logic from business logic
- Keep frontend responsible only for token storage and UX
- Use HTTPS-only secure storage mechanisms where possible
- Return consistent and predictable auth-related responses
- Log auth errors securely without leaking sensitive data
- Regularly review auth flows for security regressions

## Example Flow (Conceptual)

```text
User Signup
→ Input validation
→ Password hashing
→ User record creation
→ Success response (no sensitive data)

User Signin
→ Credential verification
→ JWT token generation
→ Token returned to client
→ Protected routes enabled
