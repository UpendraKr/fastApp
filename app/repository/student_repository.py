from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentCreate

# The repository receives the session. it does not create a session.
# The session is created in the service layer and passed to the repository.
class StudentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, student: StudentCreate) -> Student:
        db_student = Student(**student.model_dump())
        
        self.db.add(db_student)
        self.db.flush()

        return db_student