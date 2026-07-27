from app.repository.student_repository import StudentRepository
from app.schemas.student import StudentCreate
from app.tasks.email import send_email
from fastapi import BackgroundTasks


class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository
        
    def create_student(
        self,
        student: StudentCreate,
        background_tasks: BackgroundTasks,
    ):

        db = self.repository.db
        try:
            db_student = self.repository.create(student)

            db.commit()
            db.refresh(db_student)

            background_tasks.add_task(
                send_email,
                "upendra@gmail.com",
                "Student Created",
                "Student created successfully!"
                )

            return db_student

        except Exception:
            db.rollback()
            raise