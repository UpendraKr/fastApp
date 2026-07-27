# # Pydantic models
# # API request/response models (Pydantic)


# from pydantic import BaseModel, Field, EmailStr, HttpUrl

# class Address(BaseModel):
#     city: str
#     state: str


# class Course(BaseModel):
#     name: str

# # Never Use One Model Everywhere, instead use UserCreate ,UserUpdate, UserResponse, UserLogin etc
# # avoid dict if model is avilable - > address: dict now use address: Address
# class User(BaseModel):
#     name: str
#     age: int | None = None          # optional field with default value None
#     marks: int = 50                 # optional field with default value 50

#     second_name: str = Field(
#         min_length=3,
#         max_length=100
#     )

#     second_age: int = Field(
#         ge=18,
#         le=60
#     )

#     email: EmailStr
#     website: HttpUrl | None = None              # optional field with default value None

#     subjects: list[str] = Field(default=[])     # list of strings representing subjects

#     address: Address                            # nested model for address

#     courses: list[Course] = Field(default=[])      # list of nested Course objects




from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    name: str = Field( min_length=2, max_length=100 ) 
    email: EmailStr 
    password: str = Field( min_length=8 )


class UserResponse(BaseModel): 
    id: int 
    name: str 
    email: EmailStr

    model_config = { "from_attributes": True }



# Login schemas ------------------>
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel): 
    access_token: str 
    token_type: str