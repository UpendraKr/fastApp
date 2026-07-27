from fastapi import HTTPException
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User


class AuthService:

    def __init__(self, repository):
        self.repository = repository

    def register(self, request):
        existing_user = self.repository.get_by_email(
            request.email
        )

        if existing_user:
            raise HTTPException(
                status_code=409, detail="Email already registered")

        user = User(
            name=request.name,
            email=request.email,
            password_hash=hash_password(request.password)
        )
        return self.repository.create(user)

    def login(self, request):
        user = self.repository.get_by_email(request.email)
        if not user:
            raise HTTPException(
                status_code=401, detail="Invalid email or password")

        if not verify_password(request.password, user.password_hash):
            raise HTTPException(
                status_code=401, detail="Invalid email or password")

        token = create_access_token({"sub": str(user.id), "email": user.email})

        return {"access_token": token, "token_type": "bearer"}
