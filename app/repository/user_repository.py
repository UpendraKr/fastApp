from sqlalchemy import select
from app.models.user import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_by_id( self, user_id: int ): 
        stmt = select(User).where( User.id == user_id ) 
        return ( self.db.execute(stmt) .scalar_one_or_none() )

    def get_by_email(self, email: str):
        stmt = select(User).where(User.email == email)
        return (
            self.db.execute(stmt).scalar_one_or_none()
        )

    def create(self, user: User):
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
