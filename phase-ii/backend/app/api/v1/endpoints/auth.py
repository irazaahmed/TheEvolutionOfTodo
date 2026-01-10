from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from app.services.auth_service import AuthService
from app.auth.schemas import RegisterRequest, LoginRequest, LoginResponse
from app.api.deps import get_db_session
from app.auth.dependencies import security
from app.auth.jwt_service import JWTService


router = APIRouter()


@router.post("/register", response_model=LoginResponse)
async def register(
    register_data: RegisterRequest,
    db_session: AsyncSession = Depends(get_db_session)
):
    """
    Register a new user with email and password.

    Args:
        register_data: Registration request containing email and password
        db_session: Database session dependency

    Returns:
        LoginResponse containing the JWT access token
    """
    auth_service = AuthService(db_session)

    try:
        # Create new user
        user = await auth_service.register_user(register_data)

        # Create access token for the new user
        token = await auth_service.create_access_token(user.id)

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

    Args:
        login_data: Login request containing email and password
        db_session: Database session dependency

    Returns:
        LoginResponse containing the JWT access token
    """
    auth_service = AuthService(db_session)

    try:
        # Authenticate user
        user = await auth_service.authenticate_user(login_data.email, login_data.password)

        # Create access token for the authenticated user
        token = await auth_service.create_access_token(user.id)

        return LoginResponse(
            access_token=token,
            user_id=str(user.id)
        )
    except Exception as e:
        raise e