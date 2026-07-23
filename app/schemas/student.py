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



class StudentResponse(BaseModel):
    id: int
    name: str   
    age: int    
    
    model_config = {
        "from_attributes": True     
    }
