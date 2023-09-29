from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from constants import DB_ENGINE, DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


if DB_ENGINE:
    engine = create_engine(f'{DB_ENGINE}://{DB_USER}:{DB_PASS}@{DB_HOST}:'
                           f'{DB_PORT}/{DB_NAME}')
else:
    engine = create_engine('sqlite:///mydatabase.db', echo=True)

Session = sessionmaker(engine)
app = FastAPI()
Base = declarative_base()
