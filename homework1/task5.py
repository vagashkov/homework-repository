from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max = sum(nums[:k])
    counter = 0
    while counter < len(nums) - k + 1:
        if sum(nums[counter : counter + k]) > max:
            max = sum(nums[counter : counter + k])
        counter = counter + 1
    return max
