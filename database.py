"""The app's database."""
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Engine=create_engine("postgresql://kairu:112233@localhost/kairu",echo=True)

Base=declarative_base()

LocalSession=sessionmaker(bind=Engine)

