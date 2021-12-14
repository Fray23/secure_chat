from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt

from app.core import config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
    subject: Union[str, Any]
) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=config.JWT_ACCESS_TOKEN_EXPIRE_SECONDS
    )
    to_encode = {'exp': expire, 'sub': str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
