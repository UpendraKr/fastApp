from fastapi import HTTPException
from app.core.security import hash_password
from app.models.user import User


class AuthService:

    def __init__(self, repository):
        self.repository = repository

    def register(self, request):
        existing_user = self.repository.get_by_email(
            request.email
        )

        if existing_user:
            raise HTTPException(status_code=409, detail="Email already registered")

        user = User(
            name=request.name,
            email=request.email,
            password_hash=hash_password(request.password)
        )
        return self.repository.create(user)
