from datetime import datetime, timedelta
from typing import Optional
import os
from jose import JWTError, jwt
from app.core.config import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT access token with the provided data and expiration time.

    Args:
        data: Dictionary containing the claims to include in the token
        expires_delta: Optional timedelta for token expiration (defaults to 30 minutes)

    Returns:
        Encoded JWT token as string
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def verify_token(token: str):
    """
    Verify a JWT token and return the decoded payload if valid.

    Args:
        token: JWT token string to verify

    Returns:
        Decoded token payload as dictionary, or None if invalid
    """
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except JWTError:
        return None


def decode_token(token: str):
    """
    Decode a JWT token without verification (for inspection purposes only).

    Args:
        token: JWT token string to decode

    Returns:
        Decoded token payload as dictionary, or None if malformed
    """
    try:
        payload = jwt.get_unverified_claims(token)
        return payload
    except JWTError:
        return None