import pytest

from homework3.task4 import is_armstrong

test_data = [
    # False
    (10, False),
    # True
    (9, True),
    # True
    (153, True)]


@pytest.mark.parametrize("number, expected", test_data)
def test_is_armstrong(number, expected):
    """ Testing all the test data numbers one by one """
    assert is_armstrong(number) == expected
