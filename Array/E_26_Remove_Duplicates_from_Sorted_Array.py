# #26 Remove Duplicates from sorted array
#
# # Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:
#
# The judge will test your solution with the following code:
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.


# class Solution:
#     def removeDuplicates(self, nums):
#         left = 0
#         dis = 0
#         track = 0
#         while dis < len(nums):
#             while left < len(nums) - 1 and nums[left] == nums[left+1]:
#                 left += 1
#             if left >= len(nums):
#                 nums[dis] = '_'
#             else:
#                 nums[dis] = nums[left]
#                 track = dis
#
#             left += 1
#             dis += 1
#
#         return track +1

class Solution:
    def removeDuplicates(self, nums):
        left = 0
        right = 0
        track = 0
        while right < len(nums):
            if nums[left] == nums[right]:
               right += 1
            else:
               left = left + 1
               nums[left] = nums[right]


        return left + 1







nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))