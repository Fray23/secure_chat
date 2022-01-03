import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from app.core.config import DB_USER, DB_PASSWORD, DB_HOST
from app.db.base_class import Base
from app import usecases
from app.schemas.users import UserCreate


@pytest.fixture
def db_session():
    try:
        db_name = 'test'
        engine = create_engine(
            f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{db_name}'
        )
        if not database_exists(engine.url):
            create_database(engine.url)

        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = TestingSessionLocal()
        Base.metadata.create_all(bind=engine)
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def base_user(db_session):
    user = usecases.user.create(db_session, UserCreate(email='test@test.com', password='password', nick='test_nick'))
    return user
