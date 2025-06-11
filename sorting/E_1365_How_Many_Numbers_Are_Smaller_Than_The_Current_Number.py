#1365 How many numbers are smaller than the current number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller
# than it. That is, for each nums[i] you have to count the number of
# valid j's such that j != i and nums[j] < nums[i].

from typing import List
def smallerNumbers(nums: List) -> List:
    temp = sorted(nums)
    map_item = {}

    for i, x in enumerate(temp):
        if x not in map_item:
            map_item[x] = i

    return [map_item[x] for x in nums]




nums = [8, 1, 2, 2, 3]
print(smallerNumbers(nums))
