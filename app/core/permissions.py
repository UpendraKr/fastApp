from fastapi import Depends
from fastapi import HTTPException
from app.dependencies.current_user import get_current_user
from app.models.enum import UserRole


class RoleChecker:
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def __call__(
        self,
        current_user=Depends(get_current_user)
    ):
        if current_user.role not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Permission denied")
        return current_user


allow_admin = RoleChecker(
    [UserRole.ADMIN]
)

allow_teacher = RoleChecker(
    [
        UserRole.ADMIN,
        UserRole.TEACHER
    ]
)

allow_student = RoleChecker(
    [
        UserRole.ADMIN,
        UserRole.TEACHER,
        UserRole.STUDENT
    ]
)
