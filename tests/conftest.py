import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base
from app.dependencies.database import get_db
from app.core.config import settings

from main import app


test_engine = create_engine(
    settings.TEST_DATABASE_URL
)

TestingSessionLocal = sessionmaker(
    bind=test_engine,
    autoflush=False,
    autocommit=False,
)

Base.metadata.create_all(bind=test_engine)



def override_get_db():

    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    client = TestClient(app)
    return client