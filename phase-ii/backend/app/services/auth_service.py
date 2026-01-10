from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.user import User
from app.auth.schemas import RegisterRequest, LoginRequest
from app.auth.jwt_service import JWTService
from app.auth.exceptions import AuthenticationError, UserAlreadyExistsError
from passlib.context import CryptContext
import uuid


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verify a plain password against a hashed password.
        """
        return pwd_context.verify(plain_password, hashed_password)

    def hash_password(self, password: str) -> str:
        """
        Hash a plain password.
        """
        return pwd_context.hash(password)

    async def register_user(self, register_data: RegisterRequest) -> User:
        """
        Register a new user with email and password.

        Args:
            register_data: Registration request data

        Returns:
            Created User object

        Raises:
            UserAlreadyExistsError: If a user with the email already exists
        """
        # Check if user already exists
        existing_user = await self.get_user_by_email(register_data.email)
        if existing_user:
            raise UserAlreadyExistsError(detail=f"User with email {register_data.email} already exists")

        # Hash the password
        hashed_password = self.hash_password(register_data.password)

        # Create new user with email and hashed password
        user = User(
            email=register_data.email,
            hashed_password=hashed_password
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def authenticate_user(self, email: str, password: str) -> User:
        """
        Authenticate a user with email and password.

        Args:
            email: User's email address
            password: User's plain password

        Returns:
            User object if authentication is successful

        Raises:
            AuthenticationError: If authentication fails
        """
        user = await self.get_user_by_email(email)
        if not user or not self.verify_password(password, user.hashed_password):
            raise AuthenticationError(detail="Incorrect email or password")

        return user

    async def get_user_by_email(self, email: str) -> User:
        """
        Get a user by their email address.

        Args:
            email: User's email address

        Returns:
            User object if found, None otherwise
        """
        statement = select(User).where(User.email == email)
        result = await self.session.execute(statement)
        user = result.first()
        return user

    async def create_access_token(self, user_id: uuid.UUID) -> str:
        """
        Create an access token for the given user.

        Args:
            user_id: User's UUID

        Returns:
            JWT access token string
        """
        token_data = JWTService.create_token_data(user_id)
        token = JWTService.create_access_token(token_data)
        return token