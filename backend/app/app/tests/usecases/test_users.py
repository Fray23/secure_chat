import pytest
from app import usecases
from app.schemas.users import UserCreate


def test_create_user(db_session):
    email = 'test@test.com'
    password = 'strongpassword'
    user = usecases.user.create(db_session, UserCreate(email=email, password=password))
    assert user.email == 'test@test.com'


def test_authenticate(db_session, base_user):
    email = 'test@test.com'
    password = 'password'
    assert usecases.user.get_by_email(db_session, email=email) == \
           usecases.user.authenticate(db_session, password=password, email=email)


def test_fail_authenticate(db_session, base_user):
    email = 'test@test.com'
    password = 'invalid_password'
    assert usecases.user.authenticate(db_session, password=password, email=email) is None
