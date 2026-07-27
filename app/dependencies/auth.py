from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.repository.user_repository import UserRepository
from app.services.auth_service import AuthService


def get_auth_repository(
    db: Session = Depends(get_db)
):
    return UserRepository(db)


def get_auth_service(
    repository: UserRepository = Depends(get_auth_repository)
):
    return AuthService(repository)
