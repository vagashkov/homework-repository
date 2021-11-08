import pytest

from homework1.task4 import check_sum_of_four


def test_sim():
    list_a = [0, 1, 2, 3, 4]
    list_b = [4, 3, 2, 1, 0]
    list_c = [0, -1, -2, -3, 4]
    list_d = [-4, -3, -2, -1, 0]

    """Testing some hand-picked arrays"""
    assert check_sum_of_four(list_a, list_b, list_c, list_d) == 71
