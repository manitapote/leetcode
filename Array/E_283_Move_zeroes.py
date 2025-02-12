#283 Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


# class Solution:
#     def moveZeroes(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         left = 0
#         right = 0
#         while left < len(nums):
#             if nums[right] == 0:
#                 while right < len(nums) - 1 and nums[right] == 0:
#                     right += 1
#
#                 nums[left] = nums[right]
#                 nums[right] = 0
#                 right = left
#
#             right += 1
#             left += 1
#
#         return nums

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for x in range(len(nums)):
            if nums[x] != 0:
                nums[index] = nums[x]
                index += 1
        for x in range(index, len(nums)):
            nums[x] = 0

        return nums




nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))

nums = [0,0,0,3,12, 1]
print(Solution().moveZeroes(nums))
nums = [3,12, 1, 0,0,0]
print(Solution().moveZeroes(nums))

nums = [3,12, 1, 0,0,0,1,2,3]
print(Solution().moveZeroes(nums))

nums = [0]
print(Solution().moveZeroes(nums))

nums = []
print(Solution().moveZeroes(nums))
