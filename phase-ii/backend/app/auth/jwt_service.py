from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from sqlmodel.ext.asyncio.session import AsyncSession
from app.utils.jwt import verify_token, create_access_token
from app.models.user import User
from app.core.config import settings
from fastapi import HTTPException, status
from jose import JWTError
import uuid


class JWTService:
    """
    Service class to handle legacy JWT token operations including creation,
    verification, and user identity extraction.
    """

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        """
        Create an access token with the provided data.

        Args:
            data: Dictionary containing claims to include in the token
            expires_delta: Optional timedelta for token expiration

        Returns:
            Encoded JWT token string
        """
        return create_access_token(data, expires_delta)

    @staticmethod
    def verify_token(token: str) -> Optional[Dict[str, Any]]:
        """
        Verify a legacy JWT token and return the decoded payload if valid.

        Args:
            token: JWT token string to verify

        Returns:
            Decoded token payload as dictionary, or None if invalid
        """
        try:
            payload = verify_token(token)
            if payload is None:
                return None

            # Verify that the token has the required claims
            user_id = payload.get("sub")
            if user_id is None:
                return None

            return payload
        except JWTError:
            return None

    @staticmethod
    def extract_user_id_from_token(token: str) -> Optional[uuid.UUID]:
        """
        Extract user ID from a legacy JWT token.

        Args:
            token: JWT token string

        Returns:
            User ID as UUID, or None if token is invalid or user ID missing
        """
        payload = JWTService.verify_token(token)
        if payload is None:
            return None

        user_id_str = payload.get("sub")
        if user_id_str is None:
            return None

        try:
            return uuid.UUID(user_id_str)
        except ValueError:
            return None

    @staticmethod
    def create_token_data(user_id: uuid.UUID) -> Dict[str, Any]:
        """
        Create the data payload for a legacy JWT token.

        Args:
            user_id: User ID to include in the token

        Returns:
            Dictionary containing token claims
        """
        return {
            "sub": str(user_id),
            "user_id": str(user_id),
            "email": "",  # This would be populated from user data if needed
            "exp": datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes),
            "iat": datetime.utcnow(),
            "iss": "todo-app"
        }