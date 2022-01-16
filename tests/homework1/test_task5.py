import pytest

from homework1.task5 import find_maximal_subarray_sum

test_data = [
    # first sample
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
    # second sample
    ([0, 9, -11, 4, 5, 6], 2, 11),
    # third sample
    ([-1, -3, -5, -7], 3, -1),
    # fourth sample
    ([-9, -8, 8, 8, 16, -20, 0], 4, 24)
    ]


@pytest.mark.parametrize("input_list, window_size, expected", test_data)
def test_find_maximal_subarray_sum(input_list, window_size, expected):
    """ Checking each sample vs expected result """
    assert find_maximal_subarray_sum(input_list, window_size) == expected
