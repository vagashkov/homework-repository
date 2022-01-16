from homework12.models.homework_result import HomeworkResult
from homework12.models.person import Person


class DeadlineError(ValueError):
    """ custom class for too-late homeworks """
    pass


class Student(Person):
    """ class for students (uses persons table) """
    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }

    def do_homework(self, homework, solution):
        """ returns HomeWork result if work done in time
        otherwise raises the custom exception """
        if not homework.is_active():
            raise DeadlineError("You are late")
        return HomeworkResult(self, homework, solution)
