from homework5.task1 import Student, Teacher


def test_do_homework_expired(capsys):
    """ Creating and checking expired homework """
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')

    expired_homework = teacher.create_homework('Learn functions', 0)
    assert student.do_homework(expired_homework) is None
    assert capsys.readouterr().out == "You are late\n"


def test_do_homework_active():
    """ Creating and checking active homework"""
    teacher = Teacher('Daniil', 'Shadrin')

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    assert oop_homework.is_active()  # 5 days, 0:00:00
