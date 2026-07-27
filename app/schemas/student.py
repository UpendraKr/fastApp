from pydantic import BaseModel, Field, EmailStr, HttpUrl


class StudentCreate(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=100
    )

    age: int = Field(
        ge=1,
        le=60
    )

    user_id: int
    department_id: int



class StudentResponse(BaseModel):
    id: int
    name: str   
    age: int   
    user_id: int
    department_id: int 
    
    model_config = {
        "from_attributes": True     
    }


class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    user_id: int | None = None
    department_id: int | None = None
    