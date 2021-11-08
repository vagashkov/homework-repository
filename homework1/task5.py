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
        if sum(nums[counter : counter + k]) > max:
            max = sum(nums[counter : counter + k])
        counter = counter + 1
    return max
