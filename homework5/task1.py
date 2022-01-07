"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
* Update:
    progress - характеристика завершенности (от 0 до 100)
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
* Update:
    - добавлен новый параметр teacher_helps: если он равен True, то работа
    сдается в любом случае (даже просроченной)
    - добавлена вероятность выполнения домашней работы (для случая,
    когда она не просрочена и нет помощи учителя) - 80% (вычисляется на основе
    значения случайного целого числа в диапазоне от 0 до 4)
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from random import randrange


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework, teacher_helps=False):
        """ homework 'execution' routine """
        # with  teacher help homework will always be completed
        if teacher_helps:
            homework.progress = 100
            return homework
        # no help - and too late
        if not homework.is_active():
            print("You are late")
            return None
        # no help but still have time - there is a chance!
        # getting random number in range from 0 to 4
        chance = randrange(0, 4)
        # no chance (got zero) - no homework done (
        if not chance:
            return None
        # else - we hade a chance and did it!
        homework.progress = 100
        return homework


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, hw_text, hw_days):
        homework = Homework(hw_text, hw_days)
        return homework


class Homework:
    def __init__(self, text, days):
        self.text = text
        self.deadline = datetime.timedelta(days=days)
        self.created = datetime.datetime.now()
        self.progress = 0

    def is_active(self):
        now = datetime.datetime.now()
        return False if self.created + self.deadline < now else True
