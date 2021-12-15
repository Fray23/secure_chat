from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.schemas.users import UserCreate
from app.core.security import get_password_hash


class ActionUser:
    def get_by_email(self, session: Session, email: str) -> User:
        user = session.execute(select(User.email).where(User.email == email))
        return user.fetchone()

    def create(self, session: Session, obj_in: UserCreate) -> User:
        user = User(email=obj_in.email, hashed_password=get_password_hash(obj_in.password))
        session.add(user)
        session.commit()
        return user


user = ActionUser()
