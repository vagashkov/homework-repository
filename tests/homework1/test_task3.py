from homework1.task3 import find_maximum_and_minimum


def test_normal_file():
    """Testing that normal file gives us normal result"""
    assert find_maximum_and_minimum("/homework1/numbers.txt") == (111, -45)
