from app.repository.student_repository import StudentRepository
from app.schemas.student import StudentCreate
from sqlalchemy.orm import Session


class StudentService:

    def __init__(self):
        self.repository = StudentRepository()

    def create_student(self, db: Session, student: StudentCreate):
        return self.repository.create(db, student)