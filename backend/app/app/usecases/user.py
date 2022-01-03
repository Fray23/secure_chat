from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.schemas.users import UserCreate
from app.core.security import get_password_hash, verify_password


class ActionUser:
    def get_by_email(self, session: Session, email: str) -> User:
        user = session.execute(select(User).where(User.email == email)).scalar()
        return user

    def create(self, session: Session, obj_in: UserCreate) -> User:
        user = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            nick=obj_in.nick,
        )
        session.add(user)
        session.commit()
        return user

    def authenticate(self, session: Session, password: str, email: str) -> User:
        user = session.execute(select(User).where(User.email == email)).scalar()
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


user = ActionUser()
