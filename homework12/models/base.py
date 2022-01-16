from os import getcwd

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

""" performing pre-requsite operations:
- create connection to database
- create Base class for ORM-mapped entity classes """
db_file = r"sqlite:///" + getcwd() + r"/tests/homework12/main.db"
engine = create_engine(db_file)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()
