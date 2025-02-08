# # 128 Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.


# class Solution:
#     def longestConsecutive(self, nums):
#         set_nums = set(nums)
#         total = 0
#         for x in nums:
#             if x-1 not in nums:
#                 length = 0
#                 while x+length in set_nums:
#                     length += 1
#             total = max(total, length)
#         return total


class Solution:
    def longestConsecutive(self, nums) -> int:
        numbers = set(nums)
        check_done = set()
        maxLen = 0

        for num in nums:
            if num - 1 not in numbers and num not in check_done:
                length = 1

                while num + length in numbers:
                    length += 1

                maxLen = max(length, maxLen)

            check_done.add(num)

        return maxLen








# Requirements: run in O(n) and can be negative

nums = [100, 4, 200, 1, 3, 2]
a =  Solution()
print(a.longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
a =  Solution()
print(a.longestConsecutive(nums))

nums = [0,1,2, 5,6,7,8,9,100]
a =  Solution()
print(a.longestConsecutive(nums))

nums = [0,-3,7,2,5,-8,4,6,0,-1]
a =  Solution()
print(a.longestConsecutive(nums))

nums = []
a =  Solution()
print(a.longestConsecutive(nums))

nums = [0]
a =  Solution()
print(a.longestConsecutive(nums))
