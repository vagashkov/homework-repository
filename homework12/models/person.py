from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship

from homework12.models.base import Base


class Person(Base):
    """ Base class for every kind of person (incl. teachers & students"""
    __tablename__ = "person"
    # persons table columns
    person_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    type = Column(String)
    # relationships with other tables
    homeworks = relationship("Homework",
                             backref=backref("author"))
    homework_results = relationship("HomeworkResult",
                                    backref=backref("author"))
    __mapper_args__ = {
        'polymorphic_on': type,
    }

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
