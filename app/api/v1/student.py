from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.student import (
    StudentCreate,
    StudentResponse
)
from app.services.student_service import StudentService
from app.dependencies.student import get_student_service

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/", response_model=StudentResponse, status_code=201)
def create_student(
    student: StudentCreate,
    service: StudentService = Depends(get_student_service)
):

    return service.create_student(student)