from sqlalchemy import create_engine,URL
from sqlalchemy.orm import sessionmaker

from config import core

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=core.USER,
    password=core.PASS,
    database=core.NAME,
    port=core.PORT,
    host=core.HOST,
)

engine = create_engine(DATABASE_URL)

LocalSession = sessionmaker(bind=engine)

