from fastapi import Depends, HTTPException

from app.auth.dependencies import get_current_user
from app.models.enums.role import Role
from fastapi import APIRouter, Depends


class RoleChecker:

    def __init__(self, allowed_roles: list[Role]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user=Depends(get_current_user)):
        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="You don't have permission."
            )

        return current_user