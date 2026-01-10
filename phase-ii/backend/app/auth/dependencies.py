from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from app.auth.jwt_service import JWTService
import uuid


security = HTTPBearer()


async def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)) -> uuid.UUID:
    """
    Dependency to extract the current user's ID from the JWT token in the Authorization header.

    Args:
        credentials: HTTP authorization credentials containing the JWT token

    Returns:
        User ID as UUID

    Raises:
        HTTPException: If token is invalid, expired, or user ID cannot be extracted
    """
    token = credentials.credentials

    user_id = JWTService.extract_user_id_from_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user_id


async def get_optional_user_id(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)) -> Optional[uuid.UUID]:
    """
    Dependency to optionally extract the current user's ID from the JWT token.
    Returns None if no token is provided or if the token is invalid.

    Args:
        credentials: HTTP authorization credentials containing the JWT token (optional)

    Returns:
        User ID as UUID if token is valid, None otherwise
    """
    if credentials is None:
        return None

    token = credentials.credentials
    return JWTService.extract_user_id_from_token(token)