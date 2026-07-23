from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate


class StudentRepository:

    def create(self, db:Session, student: StudentCreate) -> Student:
        db_student = Student(
            name=student.name,
            age=student.age
        )
        
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student