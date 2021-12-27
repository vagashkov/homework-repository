import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Interval, String
from sqlalchemy.orm import backref, relationship

from homework12.models.base import Base


class Homework(Base):
    __tablename__ = "homework"

    homework_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("person.person_id"), nullable=False)
    text = Column(String)
    deadline = Column(Interval)
    created = Column(DateTime)
    homework_results = relationship("HomeworkResult",
                                    backref=backref("homework"))

    def __init__(self, author, text, days):
        """ Homework object constructor"""
        self.author = author
        self.text = text
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()

    def is_active(self):
        """ checking if homework is not late"""
        now = datetime.datetime.now()
        return False if self.created + self.deadline < now else True
