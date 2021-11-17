from homework3.task4 import is_armstrong


def test_armstrong_positive():
    assert is_armstrong(9)


def test_armstrong_positive_2():
    assert is_armstrong(153)


def test_armstrong_negative():
    assert not is_armstrong(10)
