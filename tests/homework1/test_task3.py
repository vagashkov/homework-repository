import pytest

from homework1.task3 import find_maximum_and_minimum

test_data = [
    # empty file
    (r"/tests/homework1/empty_numbers.txt", (0, 0)),
    # normal file
    (r"/tests/homework1/normal_numbers.txt", (111, -45)),
    # one more normal file
    (r"/tests/homework1/more_numbers.txt", (854, -371)),
    ]


@pytest.mark.parametrize("file_name, expected", test_data)
def test_find_maximum_and_minimum(file_name, expected):
    """ Checking every file vs expected result """
    assert find_maximum_and_minimum(file_name) == expected


def test_non_existing_file():
    """ Checking result for non-existing file """
    file_name = r"/tests/homework1/non_exist_numbers.txt"
    with pytest.raises(ValueError):
        find_maximum_and_minimum(file_name)
