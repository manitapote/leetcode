#905 Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

from typing import List
def sort_array_by_parity(nums: List) -> List:
    current = 0
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            nums[current], nums[i] = nums[i], nums[current]
            current += 1
    return nums





nums = [3, 1, 2, 4]
print(sort_array_by_parity(nums))

nums = [0]
print(sort_array_by_parity(nums))

nums = [0, 4,6, 3, 3, 1, 2, 4]
print(sort_array_by_parity(nums))

nums = [1, 3, 5, 4]
print(sort_array_by_parity(nums))

nums = [-1, -2, 3, 5, 4]
print(sort_array_by_parity(nums))