from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from app.auth.jwt_handler import verify_token
from app.repositories.user_repository import UserRepository
from app.database.session import get_db

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db=Depends(get_db)
):
    print("=" * 50)
    print("TOKEN:", token)

    username = verify_token(token)
    print("USERNAME:", username)

    if username is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token."
        )

    user = UserRepository.get_by_username(db, username)
    print("USER:", user)
    print("=" * 50)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found."
        )

    return user