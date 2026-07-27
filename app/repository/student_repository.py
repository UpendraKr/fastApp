from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.student import Student
from app.schemas.student import StudentCreate

# The repository receives the session. it does not create a session.
# The session is created in the service layer and passed to the repository.
class StudentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_user_id(self, user_id: int) -> Student | None:
        stmt = select(Student).where(Student.user_id == user_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def create(self, student: StudentCreate) -> Student:
        db_student = Student(**student.model_dump())
        
        self.db.add(db_student)
        self.db.flush()

        return db_student