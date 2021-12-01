from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}')

Session = sessionmaker(engine)
Base = declarative_base()
