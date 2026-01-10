# Data Model: Authentication and Security Integration

**Feature**: 2-auth-security-integration
**Created**: 2026-01-10
**Status**: Design

## Entity: Authenticated User

### Attributes
- **user_id**: UUID (Primary Identifier from JWT)
  - Type: uuid.UUID
  - Source: Extracted from JWT claims
  - Description: Unique identifier for the authenticated user

- **email**: String (from JWT)
  - Type: str
  - Source: Extracted from JWT claims
  - Description: Email address of the authenticated user

- **token_valid**: Boolean
  - Type: bool
  - Source: JWT validation result
  - Description: Indicates if the JWT token is currently valid

### Relationships
- Associated with multiple task operations through user_id

### Validation Rules
- user_id must be extracted from valid JWT claims
- token must pass signature and expiration validation

## Entity: JWT Token

### Attributes
- **token**: String (JWT)
  - Type: str
  - Source: Better Auth issuance
  - Description: JSON Web Token containing user identity claims

- **user_id**: UUID (Claim)
  - Type: uuid.UUID
  - Source: JWT payload claim
  - Description: User identifier from token claims

- **email**: String (Claim)
  - Type: str
  - Source: JWT payload claim
  - Description: Email from token claims

- **expiration**: DateTime (Claim)
  - Type: datetime.datetime
  - Source: JWT payload claim (exp)
  - Description: Token expiration time

- **issuer**: String (Claim)
  - Type: str
  - Source: JWT payload claim (iss)
  - Description: Token issuer identifier

### Validation Rules
- Token must have valid signature
- Token must not be expired at time of validation
- Required claims (user_id, exp) must be present
- Signature must match configured verification key

## Entity: Secure Task Operation

### Attributes
- **operation_type**: String
  - Type: str (CREATE, READ, UPDATE, DELETE, TOGGLE)
  - Description: Type of task operation being performed

- **authenticated_user_id**: UUID
  - Type: uuid.UUID
  - Source: JWT claim extraction
  - Description: User ID from validated JWT token

- **target_task_user_id**: UUID
  - Type: uuid.UUID
  - Source: Task entity user_id field
  - Description: User ID associated with the target task

- **authorized**: Boolean
  - Type: bool
  - Computed: authenticated_user_id == target_task_user_id
  - Description: Whether the operation is authorized

### Validation Rules
- authenticated_user_id must match target_task_user_id for operation to proceed
- Operation must be rejected if authorization check fails

## State Transitions

### JWT Validation
- **From**: Unverified token state
- **To**: Validated/Invalid token state
- **Trigger**: JWT validation process
- **Validation**: Token signature, expiration, and claim integrity

### Authorization Check
- **Action**: Secure task operation attempt
- **Validation**: Compare authenticated user ID with task owner ID
- **Result**: Allow operation if IDs match, deny if they differ

## Indexes

### JWT Validation Cache (Conceptual)
- For performance: Cache recently validated tokens with short TTL
- Prevent replay attacks and enforce revocation if needed