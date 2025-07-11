from typing import List
class Solution:
    def maximumStrongPairXor(self,
                             nums: List[int]
                             ) -> int:
        left = 0
        result = 0
        while left < len(nums):
            right = left
            while right < len(nums):
                if abs(nums[left] - nums[right]) <= min(nums[left], nums[right]):
                    result = max(result, nums[left]^nums[right])
                right += 1

            left += 1


        return result






#|x - y| <= min(x, y)
nums = [1, 2, 3, 4, 5]
print(Solution().maximumStrongPairXor(nums))
nums = [10,100]
print(Solution().maximumStrongPairXor(nums))