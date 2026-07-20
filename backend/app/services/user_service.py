from sqlalchemy.orm import Session

from app.auth.jwt_handler import create_access_token
from app.auth.password import hash_password, verify_password
from app.models.enums import role
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.exceptions.custom_exception import DuplicateStudentException
from app.auth.jwt_handler import create_access_token
from app.auth.password import verify_password
from app.exceptions.custom_exception import InvalidCredentialsException
from app.models.enums.role import Role


class UserService:

    @staticmethod
    def register(db: Session, request: UserCreate):

        if UserRepository.get_by_username(db, request.username):
            raise DuplicateStudentException(
                "Username already exists."
            )

        if UserRepository.get_by_email(db, request.email):
            raise DuplicateStudentException(
                "Email already exists."
            )

        user = User(
            username=request.username,
            full_name=request.full_name,
            email=request.email,
            password=hash_password(request.password),
            role= Role.USER
        )

        return UserRepository.create(db, user)

    @staticmethod
    def login(
            db: Session,
            username: str,
            password: str
    ):
        user = UserRepository.get_by_username(
            db,
            username
        )

        if not user:
            raise InvalidCredentialsException(
                "Invalid username or password."
            )

        if not verify_password(
                password,
                user.password
        ):
            raise InvalidCredentialsException(
                "Invalid username or password."
            )

        access_token = create_access_token(
            {
                "sub": user.username
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }