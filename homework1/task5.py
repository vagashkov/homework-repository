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
    max = sum(nums[:k])
    counter = 0
    # browse through the sequence
    while counter < len(nums) - k + 1:
        # some k-member aequence sum
        # is greater than prevous maximum -
        # so redefine it
        if sum(nums[counter:counter + k]) > max:
            max = sum(nums[counter:counter + k])
        counter = counter + 1
    return max
