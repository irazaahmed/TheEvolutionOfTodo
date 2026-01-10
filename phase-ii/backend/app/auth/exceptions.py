from fastapi import HTTPException, status


class AuthenticationError(HTTPException):
    """
    Exception raised when authentication fails.
    """
    def __init__(self, detail: str = "Authentication failed"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


class AuthorizationError(HTTPException):
    """
    Exception raised when authorization fails (valid token but insufficient privileges).
    """
    def __init__(self, detail: str = "Not enough permissions"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )


class TokenValidationError(HTTPException):
    """
    Exception raised when token validation fails.
    """
    def __init__(self, detail: str = "Token validation failed"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


class UserNotFoundError(HTTPException):
    """
    Exception raised when a user is not found.
    """
    def __init__(self, detail: str = "User not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )


class UserAlreadyExistsError(HTTPException):
    """
    Exception raised when a user already exists during registration.
    """
    def __init__(self, detail: str = "User already exists"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail
        )