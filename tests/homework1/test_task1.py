import pytest

from homework1.task1 import check_power_of_2

test_data = [
    # False: negative number
    (-15, False),
    # False: zero number
    (0, False),
    # True: 1 is 2 powered to 0
    (1, True),
    # False: odd number
    (33, False),
    # False: even number
    (42, False),
    # True: positive example
    (65536, True)]


@pytest.mark.parametrize("number, expected", test_data)
def test_check_power_of_2(number, expected):
    """ Testing all the test data numbers one by one """
    assert check_power_of_2(number) == expected
