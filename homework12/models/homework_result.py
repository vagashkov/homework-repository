from sqlalchemy import Column, ForeignKey, Integer, String

from homework12.models.base import Base
from homework12.models.homework import Homework


class HomeworkResult(Base):
    __tablename__ = "homework_result"

    homework_result_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("person.person_id"), nullable=False)
    homework_id = Column(Integer,
                         ForeignKey("homework.homework_id"), nullable=False)
    solution = Column(String)

    def __init__(self, author, homework, solution):
        """ homework_result object constructor check if
        homework object is of a proper type and raises an exception
        if it isn't"""
        if not isinstance(homework, Homework):
            raise ValueError("You gave a not Homework object")
        self.author = author
        self.homework = homework
        self.solution = solution

    def __eq__(self, other):
        return (other and self.author == other.author
                and self.homework == other.homework
                and self.solution == other.solution)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.author, self.homework, self.solution))
