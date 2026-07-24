from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.repository.student_repository import StudentRepository
from app.services.student_service import StudentService


def get_student_repository(
    db: Session = Depends(get_db)
):
    return StudentRepository(db)

def get_student_service(
    repository: StudentRepository = Depends(get_student_repository)
):
    return StudentService(repository)