from fastapi import FastAPI, Depends
from pydantic import BaseModel
from app.schemas.user import User
from app.dependencies.settings import get_settings
from app.dependencies.current_user import get_current_user
from app.dependencies.database import get_db
from app.core.config import settings
from app.core.handlers import register_exception_handlers
from app.core.middleware import RequestTimingMiddleware
from app.core.logging_config import configure_logging
from app.api.v1.student import router as student_router

# Configure logging before anything emits log records.
configure_logging()

# inbuilt FastAPI middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Custom request-timing middleware (added first so it wraps the outermost layer)
app.add_middleware(RequestTimingMiddleware)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Add GZip middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],
)

register_exception_handlers(app)

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
