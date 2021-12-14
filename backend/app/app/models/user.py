from sqlalchemy import Column, Integer, String
from app.db.base_class import Base


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    nick = Column(String(30))
    email = Column(String(40), unique=True)
    hashed_password = Column(String(100))
