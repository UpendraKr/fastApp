from sqlalchemy import String, Integer, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base
from datetime import datetime


class Enrollment(Base): 
    __tablename__ = "enrollments" 
    
    id: Mapped[int] = mapped_column(primary_key=True) 
    
    student_id: Mapped[int] = mapped_column( ForeignKey("students.id") ) 
    course_id: Mapped[int] = mapped_column( ForeignKey("courses.id") ) 
    semester: Mapped[int] 
    grade: Mapped[str | None] 
    
    enrolled_at: Mapped[datetime] 
    student = relationship( "Student", back_populates="enrollments" ) 
    course = relationship( "Course", back_populates="enrollments" )