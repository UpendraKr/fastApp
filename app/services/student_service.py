from app.repository.student_repository import StudentRepository
from app.schemas.student import StudentCreate


class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def create_student(self, student: StudentCreate):

        db = self.repository.db
        try:
            db_student = self.repository.create(student)

            db.commit()
            db.refresh(db_student)

            return db_student

        except Exception:
            db.rollback()
            raise