from fastapi import Depends, HTTPException

from app.core.oauth2 import oauth2_scheme
from app.core.security import decode_access_token
from app.dependencies.auth import get_auth_repository
from app.repository.user_repository import UserRepository


def get_current_user(
        token: str = Depends(oauth2_scheme),
        repo: UserRepository = Depends(get_auth_repository)
):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = repo.get_by_id(int(payload["sub"]))

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user
