from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse, UserRegister, TokenResponse, UserLogin
from app.services.auth_service import AuthService

from app.dependencies.auth import get_auth_service
from app.dependencies.current_user import get_current_user

from app.models.user import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse, status_code=201)
def register(
    request: UserRegister,
    service: AuthService = Depends(get_auth_service)
):

    return service.register(request)


@router.post("/login", response_model=TokenResponse)
def login(
    request: UserLogin,
    service: AuthService = Depends(get_auth_service)
):
    return service.login(request)


# /api/v1/auth/me
@router.get("/me", response_model=UserResponse)
def me(
    current_user: User = Depends(get_current_user)
):
    return current_user
