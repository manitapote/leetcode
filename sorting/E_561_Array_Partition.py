# 561 Array Partition
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.
# Return the maximized sum.

from typing import List
def maximize_sum(nums: List) -> int:
    if len(nums) == 0:
        return 0

    nums.sort()

    return sum(nums[::2])

nums = [1, 4, 3, 2]
print(maximize_sum(nums))

nums = [6,2,6,5,1,2]
print(maximize_sum(nums))
