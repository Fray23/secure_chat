from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(40), unique=True)
    hashed_password = Column(String(100))
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

