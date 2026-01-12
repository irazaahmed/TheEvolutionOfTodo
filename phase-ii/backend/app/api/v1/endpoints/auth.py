from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from app.services.auth_service import AuthService
from app.auth.schemas import RegisterRequest, LoginRequest, LoginResponse
from app.api.deps import get_db_session
from app.auth.dependencies import security, get_current_user_id
from app.auth.jwt_service import JWTService
from app.core.config import settings
from jose import jwt
from datetime import datetime, timedelta
import uuid


router = APIRouter()


@router.post("/register", response_model=LoginResponse)
async def register(
    register_data: RegisterRequest,
    db_session: AsyncSession = Depends(get_db_session)
):
    """
    Register a new user with email and password.
    Returns a token compatible with Better Auth format.

    Args:
        register_data: Registration request containing email and password
        db_session: Database session dependency

    Returns:
        LoginResponse containing the JWT access token in Better Auth format
    """
    auth_service = AuthService(db_session)

    try:
        # Create new user
        user = await auth_service.register_user(register_data)

        # Create access token in Better Auth compatible format
        token_data = {
            "userId": str(user.id),  # Better Auth expects userId field
            "email": user.email,
            "exp": datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes),
            "iat": datetime.utcnow(),
            "iss": "todo-app-better-auth"
        }

        token = jwt.encode(token_data, settings.secret_key, algorithm=settings.algorithm)

        return LoginResponse(
            access_token=token,
            user_id=str(user.id)
        )
    except Exception as e:
        raise e


@router.post("/login", response_model=LoginResponse)
async def login(
    login_data: LoginRequest,
    db_session: AsyncSession = Depends(get_db_session)
):
    """
    Authenticate a user with email and password.
    Returns a token compatible with Better Auth format.

    Args:
        login_data: Login request containing email and password
        db_session: Database session dependency

    Returns:
        LoginResponse containing the JWT access token in Better Auth format
    """
    auth_service = AuthService(db_session)

    try:
        # Authenticate user
        user = await auth_service.authenticate_user(login_data.email, login_data.password)

        # Create access token in Better Auth compatible format
        token_data = {
            "userId": str(user.id),  # Better Auth expects userId field
            "email": user.email,
            "exp": datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes),
            "iat": datetime.utcnow(),
            "iss": "todo-app-better-auth"
        }

        token = jwt.encode(token_data, settings.secret_key, algorithm=settings.algorithm)

        return LoginResponse(
            access_token=token,
            user_id=str(user.id)
        )
    except Exception as e:
        raise e


@router.get("/session")
async def get_session(
    current_user_id: uuid.UUID = Depends(get_current_user_id)
):
    """
    Get the current user session information.
    This endpoint is used by the frontend to verify the token and get user data.

    Args:
        current_user_id: The authenticated user ID extracted from the token

    Returns:
        User information including ID and email
    """
    # For now, we just return the user ID since we don't have a user service to fetch full user details
    # In a real implementation, you'd fetch the user from the database
    return {
        "userId": str(current_user_id),
        "user_id": str(current_user_id),  # For backward compatibility
        "email": "user@example.com"  # This would come from the user database in a real implementation
    }