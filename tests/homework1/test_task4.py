import pytest

from homework1.task4 import check_sum_of_four

test_data = [
    # first sample
    (
        [0, 1],  # list a
        [4, 3],  # list b
        [4, 3],  # list c
        [-4, -3],  # list d
        0
    ),
    # second sample
    (
        [0, 1, 2],  # list a
        [4, 3, 2],  # list b
        [4, 3, 2],  # list c
        [-4, -3, -2],  # list d
        1
    ),
    # third sample
    (
        [0, 1, 2, 3],  # list a
        [4, 3, 2, 1],  # list b
        [4, 3, 2, 1],  # list c
        [-4, -3, -2, -1],  # list d
        10
    ),
    # fourth sample
    (
        [0, 1, 2, 3, 4],  # list a
        [4, 3, 2, 1, 0],  # list b
        [4, 3, 2, 1, 0],  # list c
        [-4, -3, -2, -1, 0],  # list d
        35
    )
    ]


@pytest.mark.parametrize("list_a, list_b, list_c, list_d, expected", test_data)
def test_check_sum_of_four(list_a, list_b, list_c, list_d, expected):
    """ Checking every sample vs expected result """
    assert check_sum_of_four(list_a, list_b, list_c, list_d) == expected
