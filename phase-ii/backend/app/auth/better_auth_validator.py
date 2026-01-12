from datetime import datetime
from typing import Optional, Dict, Any
from sqlmodel.ext.asyncio.session import AsyncSession
from app.utils.jwt import verify_token
from app.models.user import User
from app.core.config import settings
from fastapi import HTTPException, status
from jose import JWTError, jwt
from datetime import datetime
import uuid


class BetterAuthValidator:
    """
    Validator for Better Auth JWT tokens.
    This class provides methods to verify Better Auth issued tokens and extract user information.
    """

    @staticmethod
    def verify_better_auth_token(token: str) -> Optional[Dict[str, Any]]:
        """
        Verify a Better Auth JWT token and return the decoded payload if valid.

        Args:
            token: JWT token string to verify

        Returns:
            Decoded token payload as dictionary, or None if invalid
        """
        try:
            # Verify token using the same secret as used for signing
            payload = jwt.decode(
                token,
                settings.secret_key,
                algorithms=[settings.algorithm]
            )

            # Verify that the token has the required claims expected by Better Auth
            user_id = payload.get("userId") or payload.get("sub")
            if user_id is None:
                return None

            return payload
        except JWTError:
            return None

    @staticmethod
    def extract_user_id_from_better_auth_token(token: str) -> Optional[uuid.UUID]:
        """
        Extract user ID from a Better Auth JWT token.

        Args:
            token: JWT token string

        Returns:
            User ID as UUID, or None if token is invalid or user ID missing
        """
        payload = BetterAuthValidator.verify_better_auth_token(token)
        if payload is None:
            return None

        # Better Auth typically stores user ID as "userId" in the token
        user_id_str = payload.get("userId") or payload.get("sub")
        if user_id_str is None:
            return None

        try:
            return uuid.UUID(user_id_str)
        except ValueError:
            return None