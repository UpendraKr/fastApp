from fastapi import FastAPI, Depends
from pydantic import BaseModel
from app.schemas.user import User
from app.dependencies.settings import get_settings
from app.dependencies.current_user import get_current_user
from app.dependencies.database import get_db
from app.core.config import settings
from app.api.v1.student import router as student_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(student_router, prefix="/api/v1")

@app.get("/")
def home():
    return {"Hello": "World"}


@app.post("/users")
def create_user(user: User):
    return user


@app.get("/dashboard")
def get_users(
    settings=Depends(get_settings),
    current_user=Depends(get_current_user),
    db=Depends(get_db)
):
    return {
        "settings": settings,
        "current_user": current_user,
        "db": db
    }
