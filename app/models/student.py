from sqlalchemy import String, Integer, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


student_courses = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", ForeignKey("students.id",
           ondelete="CASCADE"), primary_key=True),
    Column("course_id", ForeignKey("courses.id",
           ondelete="CASCADE"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer())

    # One-to-One
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user = relationship(
        "User",
        back_populates="student"
    )

    # One-to-Many
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))
    department = relationship(
        "Department",
        back_populates="students"
    )

    # Many-to-Many
    courses = relationship(
        "Course",
        secondary=student_courses,
        back_populates="students"
    )


    enrollments = relationship( "Enrollment", back_populates="student" )