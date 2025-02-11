# #169 Majority Element
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
import math


# class Solution:
#     def majorityElement(self, nums):
#         if len(nums) == 1:
#             return nums[0]
#
#         max_count = len(nums) /2
#         track = {}
#         for x in nums:
#             if x in track:
#                 track[x] += 1
#                 if track[x] > max_count:
#                     return x
#             else:
#                 track[x] = 1


class Solution:
    def majorityElement(self, nums):
        nums.sort()
        max_index = math.floor(len(nums)/2)

        return nums[max_index]






nums = [3,2,3]
a = Solution()
print(a.majorityElement(nums))

nums = [2,2,1,1,1,2,2]
a = Solution()
print(a.majorityElement(nums))


