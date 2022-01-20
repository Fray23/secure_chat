import pytest
from app import usecases
from app.schemas.users import UserCreate


def test_create_user(db_session):
    nickname = 'test_nickname'
    password = 'strongpassword'
    user = usecases.user.create(db_session, UserCreate(nickname=nickname, password=password))
    assert user.nickname == nickname


def test_authenticate(db_session, base_user):
    nickname = 'test_nickname'
    password = 'password'
    assert usecases.user.get_by_nickname(db_session, nickname=nickname) == \
           usecases.user.authenticate(db_session, password=password, nickname=nickname)


def test_fail_authenticate(db_session, base_user):
    nickname = 'test_nickname'
    password = 'invalid_password'
    assert usecases.user.authenticate(db_session, password=password, nickname=nickname) is None
