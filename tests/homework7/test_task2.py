import pytest

from homework7.task2 import backspace_compare

test_data = [
    # True: both strings become "ac"
    ("ab#c", "ad#c", True),
    # True: both strings become "c"
    ("a##c", "#a#c", True),
    # False: first becomes "c" while second becomes "b".
    ("a#c", "b", False),
    # True: first becomes empty, second is already empty
    ("###", "", True)]


@pytest.mark.parametrize("first, second, expected", test_data)
def test_backspace_compare(first, second, expected):
    """ loading parametrized test for all the typical cases"""
    assert(backspace_compare(first, second) == expected)
