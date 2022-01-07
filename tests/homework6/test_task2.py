import pytest

from homework6.task2 import HomeworkResult, Student, Teacher


def test_homeworks_done(capsys):
    """ testing the wull scenario"""

    # create two teachers and two students
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')
    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    # create two homeworks
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    # creating four homework results:
    # - two should be accepted and cached
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    # two will be rejected (first due to wrong (too short) solution
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    result_4 = None
    # check if ValueError is raised if we provide not a homework
    # object in order tp create HomeworkResult
    with pytest.raises(ValueError):
        result_4 = HomeworkResult(good_student, "fff", "Solution")
        assert not result_4

    # checking first homework result twice
    opp_teacher.check_homework(result_1, 5)
    # accepted homework result should be cached
    temp_1 = opp_teacher.homework_done
    # checking it one more time
    advanced_python_teacher.check_homework(result_1, 5)
    temp_2 = Teacher.homework_done
    # there should be only one instance of rezult_1
    # in common homework_results storage
    assert temp_1 is temp_2

    # check two more homework_results
    # result_2 will be ok and added to common storage
    # result_3 should be rejected
    opp_teacher.check_homework(result_2, 4)
    opp_teacher.check_homework(result_3, 5)

    # checking if oop_hw result is in storage
    assert isinstance(Teacher.homework_done[oop_hw], HomeworkResult)
    # checking that common storage is empty after being reset
    Teacher.reset_results()
    assert not Teacher.homework_done
