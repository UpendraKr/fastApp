from sqlalchemy import String, Integer, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base


class Department(Base): 
    
    __tablename__="departments" 
    
    id: Mapped[int] = mapped_column(primary_key=True) 
    name: Mapped[str] 
    
    students = relationship( "Student", back_populates="department" )