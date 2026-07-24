from fastapi import APIRouter, Depends, Path, Query, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, Literal
from sqlalchemy import select

from app.dependencies.database import get_db
from app.schemas.student import (
    StudentCreate,
    StudentResponse, 
    StudentUpdate
)
from app.models.student import Student
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


@router.get("/", response_model=list[StudentResponse], status_code=200)
def get_student(
    db: Session = Depends(get_db),
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1, le=100)] = 10,
    search: Annotated[str | None, Query(min_length=2)] = None,
    sort: Annotated[
        Literal["id", "name", "age"],
        Query()
    ] = "id",
    order: Annotated[
        Literal["asc", "desc"],
        Query()
    ] = "asc"
):

    offset = (page - 1) * size
    stmt = select(Student)

    if search:
        stmt = stmt.where(
            Student.name.ilike(f"%{search}%")
        )

    column = getattr(Student, sort)

    if order == "desc":
        stmt = stmt.order_by(column.desc())
    else:
        stmt = stmt.order_by(column.asc())

    stmt = stmt.offset(offset).limit(size)
    students = db.execute(stmt).scalars().all()

    return students;


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: Annotated[
        int,
        Path(
            gt=0,
            description="Student ID",
            example=1
        )
    ],
    db: Session = Depends(get_db)
):
    stmt = select(Student).where(Student.id == student_id)
    student = db.execute(stmt).scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student



@router.patch( "/{student_id}", response_model=StudentResponse )
def update_student( 
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    stmt = select(Student).where(Student.id == student_id)
    db_student = db.execute(stmt).scalar_one_or_none()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student.dict(exclude_unset=True).items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)

    return db_student