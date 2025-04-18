# 26. Remove Duplicates from Sorted Array
#
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution:
    def removeDuplicates(self, nums) -> int:
        past_obv_index = 1

        for i in range(len(nums)):
            if i == 0:
                i += 1
                continue

            if nums[past_obv_index] != nums[i]:
                nums[past_obv_index] = nums[i]
                past_obv_index += 1

        nums[past_obv_index:] = '_'

        return past_obv_index

nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]
a = Solution()
print(a.removeDuplicates(nums))

