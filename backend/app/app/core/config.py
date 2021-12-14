import os

DEBUG = os.getenv('DEBUG', '').lower() == 'true'

DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_DATABASE = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_LINK = f'{DB_HOST}:{DB_PORT}'
