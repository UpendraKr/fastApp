from app.repository.student_repository import StudentRepository
from app.repository.user_repository import UserRepository
from app.schemas.student import StudentCreate
from app.tasks.email import send_email
from fastapi import BackgroundTasks


class StudentService:

    def __init__(self, repository: StudentRepository, user_repo: UserRepository):
        self.repository = repository
        self.user_repo = user_repo
        
    def create_student(
        self,
        student: StudentCreate,
        background_tasks: BackgroundTasks,
    ):

        user = self.user_repo.get_by_id(student.user_id)

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        existing_student = self.repository.get_by_user_id(
            student.user_id
        )

        if existing_student:
            raise HTTPException(
                status_code=409,
                detail="Student profile already exists"
            )


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