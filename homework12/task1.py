"""
Using ORM framework of your choice,
create models classes created in Homework 6
(Teachers, Students, Homework and others).
- Target database should be sqlite
(filename main.db localted in current directory)
- ORM framework should support migrations.

Utilizing that framework capabilities, create
a migration file, creating all necessary database structures.
a migration file (separate) creating at least one record
in each created database table
(*) optional task: write standalone script (get_report.py)
that retrieves and stores the following information into
CSV file report.csv
for all done (completed) homeworks:
Student name (who completed homework)
Creation date
Teacher name who created homework
Utilize ORM capabilities as much as possible,
avoiding executing raw SQL queries.
"""

from homework12.models.base import Base, engine, session
from homework12.models.homework import Homework
from homework12.models.homework_result import HomeworkResult
from homework12.models.person import Person
from homework12.models.student import Student
from homework12.models.teacher import Teacher


def create_tables():
    table_list = [Person.__table__,
                  Homework.__table__,
                  HomeworkResult.__table__]
    Base.metadata.create_all(engine, tables=table_list)


def populate_tables():
    # we need student to execute homework
    student = Student("Roman", "Petrov")
    session.add(student)
    # and teacher to create it and check result
    teacher = Teacher("Daniil", "Shadrin")
    session.add(teacher)
    # let's create two homeworks
    oop_hw = teacher.create_homework('Learn OOP', 1)
    docs_hw = teacher.create_homework('Read docs', 5)
    session.add(oop_hw)
    session.add(docs_hw)
    # and execute it
    oop_hw_result = student.do_homework(oop_hw, 'I have done this hw')
    docs_hw_result = student.do_homework(docs_hw, 'I have done this hw too')
    session.add(oop_hw_result)
    session.add(docs_hw_result)
    # than teacher can check it
    teacher.check_homework(oop_hw_result)
    teacher.check_homework(docs_hw_result)
    session.commit()


if __name__ == '__main__':
    create_tables()
    populate_tables()
