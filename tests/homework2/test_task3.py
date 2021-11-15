from homework2.task3 import combinations


def test_combinations():
    """Testing HW example"""
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]
