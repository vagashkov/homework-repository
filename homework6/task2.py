"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class Person:
    """ Base class for every kind of person (incl. teachers & students"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    """" returns HomeWork result if work done in time
    otherwise raises the custom exception """
    def do_homework(self, homework, solution):
        if not homework.is_active():
            raise DeadlineError("You are late")
        return HomeworkResult(self, homework, solution)


class Teacher(Person):
    """ class Teacher includes common (class-wide)
    storage for homework_results that passed control.
    It uses defaultdict type using HomeworkResult object as a key
    to ensure homework results uniqueness"""
    homework_done = defaultdict(list)

    def create_homework(self, hw_text, hw_days):
        """ creating new homewors objects"""
        homework = Homework(hw_text, hw_days)
        return homework

    def check_homework(self, homework_result, grade):
        """ checking if homework is done properly
        (its solution text is longer than 5 characters"""
        if len(homework_result.solution) > 5:
            # put grade into HomeworkResult object
            homework_result.grade = grade
            # storing HomeworkResult object in a dict
            self.homework_done[homework_result.homework] = homework_result
            return True
        return False

    @classmethod
    def reset_results(cls):
        """ clearing the HomeworkResult object storage"""
        cls.homework_done.clear()


class DeadlineError(Exception):
    """ custom class for exception"""
    pass


class Homework:
    def __init__(self, text, days):
        """ Homework object constructor"""
        self.text = text
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()

    def is_active(self):
        """ checking if homework is not late"""
        now = datetime.datetime.now()
        return False if self.created + self.deadline < now else True


class HomeworkResult:
    def __init__(self, author, homework, solution):
        """ homework_result object constructor check if
        homework object is of a proper type and raises an exception
        if it isn't"""
        if not isinstance(homework, Homework):
            raise ValueError("You gave a not Homework object")
        self.author = author
        self.homework = homework
        self.solution = solution
        self.grade = 0
