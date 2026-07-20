from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import UserService
from app.schemas.auth_schema import LoginRequest, TokenResponse
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
        request: UserCreate,
        db: Session = Depends(get_db)
):
    return UserService.register(db, request)

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return UserService.login(
        db,
        form_data.username,
        form_data.password
    )