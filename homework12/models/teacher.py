from collections import defaultdict

from homework12.models.homework import Homework
from homework12.models.person import Person


class Teacher(Person):
    """ class Teacher includes common (class-wide)
    storage for homework_results that passed control.
    It uses defaultdict type using HomeworkResult object as a key
    to ensure homework results uniqueness"""
    homework_done = defaultdict(list)

    __mapper_args__ = {
        'polymorphic_identity': 'teacher',
    }

    def create_homework(self, hw_text, hw_days):
        """ creating new homewors objects"""
        homework = Homework(self, hw_text, hw_days)
        return homework

    def check_homework(self, homework_result):
        """ checking if homework is done properly
        (its solution text is longer than 5 characters"""
        if len(homework_result.solution) > 5:
            # storing HomeworkResult object in a dict
            self.homework_done[homework_result.homework] = homework_result
            return True
        return False
