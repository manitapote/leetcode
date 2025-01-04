# 169. Majority Element
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums) -> int:
        candidate = None
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
                count = 1
                continue
            if x == candidate:
                count +=1
            else:
                count -=1


        return candidate

import math

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()      #Time complexity is O(nlog(n))
#
#         n = (len(nums) // 2)
#
#         if nums[n] == nums[n-1]:
#             return nums[n-1]
#         else:
#             return nums[n+1]
#
nums = [2,2,1,1,1,2,2]
a = Solution()
print(a.majorityElement(nums))



