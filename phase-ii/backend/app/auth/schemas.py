from pydantic import BaseModel
from typing import Optional
import uuid


class Token(BaseModel):
    """
    Schema for JWT token response.
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Schema for token data containing user information.
    """
    user_id: Optional[str] = None
    email: Optional[str] = None


class LoginRequest(BaseModel):
    """
    Schema for login request.
    """
    email: str
    password: str


class RegisterRequest(BaseModel):
    """
    Schema for registration request.
    """
    email: str
    password: str
    username: Optional[str] = None


class LoginResponse(BaseModel):
    """
    Schema for login response containing the JWT token.
    """
    access_token: str
    token_type: str = "bearer"
    user_id: str