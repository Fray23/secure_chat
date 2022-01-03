import pytest
from app import usecases
from app.core.security import verify_password, create_access_token
from app.schemas.users import UserCreate


def test_verify_password(db_session):
    email = 'test@test.com'
    password = 'strongpassword'
    user = usecases.user.create(db_session, UserCreate(email=email, password=password))
    assert verify_password(password, user.hashed_password)


def test_incorrect_verify_password(db_session):
    email = 'test@test.com'
    password = 'strongpassword'
    incorrect_password = 'incorrect_password'
    user = usecases.user.create(db_session, UserCreate(email=email, password=password))
    assert not verify_password(incorrect_password, user.hashed_password)


def test_create_access_token(db_session):
    token = create_access_token(subject={'email': 'sometest@test.com'})
