#217 Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))



nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))
nums = [1,2,3,4]
print(Solution().containsDuplicate(nums))
nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))