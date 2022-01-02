"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    # setting initial 'max' value
    max_sum = max(nums)
    # browse through the sequence
    # starting from the most narrow (length = 1)
    # to the most wide (length = k) window
    for window_len in range(1, k+1):
        counter = 0
        while counter < len(nums) - window_len + 1:
            # some "window_len"-member sequence sum
            # is greater than prevous maximum -
            # so redefine it
            if sum(nums[counter:counter + window_len]) > max_sum:
                max_sum = sum(nums[counter:counter + k])
            counter = counter + 1
    return max_sum
