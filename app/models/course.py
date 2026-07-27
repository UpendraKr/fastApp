from app.db.database import Base
from sqlalchemy import String, Integer, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.student import student_courses



class Course(Base):

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    creadits: Mapped[int]

    students = relationship(
        "Student",
        secondary=student_courses,
        back_populates="courses"
    )

    enrollments = relationship( "Enrollment", back_populates="course" )