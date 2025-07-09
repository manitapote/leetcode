from typing import List
class Solution:
    def maximumUniqueSubarray(self,
                              nums: List[int]
                              ) -> int:
        numbers = set()
        if len(numbers) == len(nums):
            return sum(numbers)
        maxval = float('-inf')
        total = sum(nums)
        for i in range(0, len(nums)):
            if nums[i] not in numbers:
                numbers.add(nums[i])





nums = [4, 2, 4, 5, 6]
print(Solution().maximumUniqueSubarray(nums))
nums = [5,2,1,2,5,2,1,2,5]
print(Solution().maximumUniqueSubarray(nums))

