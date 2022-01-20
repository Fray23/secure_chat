import pytest
from app import usecases
from app.core.security import verify_password
from app.schemas.users import UserCreate


def test_verify_password(db_session):
    nickname = 'test@test.com'
    password = 'strongpassword'
    user = usecases.user.create(db_session, UserCreate(nickname=nickname, password=password))
    assert verify_password(password, user.hashed_password)


def test_incorrect_verify_password(db_session):
    nickname = 'test@test.com'
    password = 'strongpassword'
    incorrect_password = 'incorrect_password'
    user = usecases.user.create(db_session, UserCreate(nickname=nickname, password=password))
    assert not verify_password(incorrect_password, user.hashed_password)
