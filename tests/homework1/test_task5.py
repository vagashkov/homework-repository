from homework1.task5 import find_maximal_subarray_sum


def test_array1():
    """Testing normal sample"""
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 16
