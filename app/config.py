from os import getenv
from uuid import uuid4

from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = getenv('SECRET_KEY')

JWT_SECRET = str(uuid4())
JWT_ALGORITHM = 'HS256'
JWT_EXPIRE_MINUTES = 60

DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_NAME = getenv('DB_NAME')
DB_HOST = 'postgres_db'
DB_PORT = '5432'

SQLALCHEMY_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)

ADMIN_NAME = getenv('ADMIN_NAME')
ADMIN_PASSWORD = getenv('ADMIN_PASSWORD')
ADMIN_EMAIL = getenv('ADMIN_EMAIL')
