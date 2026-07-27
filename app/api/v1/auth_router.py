from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse, UserRegister
from app.services.auth_service import AuthService

from app.dependencies.auth import get_auth_service


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
