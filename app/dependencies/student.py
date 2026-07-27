from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.repository.student_repository import StudentRepository
from app.repository.user_repository import UserRepository
from app.services.student_service import StudentService
from app.dependencies.auth import get_auth_repository

def get_student_repository(
    db: Session = Depends(get_db)
):
    return StudentRepository(db)

def get_student_service(
    repository: StudentRepository = Depends(get_student_repository),
    user_repo: UserRepository = Depends(get_auth_repository)
):
    return StudentService(repository, user_repo)