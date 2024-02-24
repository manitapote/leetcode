# class Solution(object):
#     def smallerNumbersThanCurrent(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         b = []
#         for i in range(len(nums)):
#             a = 0
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 if nums[i] > nums[j]:
#                     a += 1
#             b.append(a)
#
#         return b
# #time complexity O(n^2)
#space complexity O(n)
#313ms

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):

        pass



# a = [8,1,2,2,3]
a = [6,5,4,8]
b = Solution()

result = b.smallerNumbersThanCurrent(a)
print(result)