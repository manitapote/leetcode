# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         result = []
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 if i > j:
#                     continue
#                 if nums[i] == nums[j]:
#                     result.append((i, j))
#
#         return len(result)

#13 ms
# time : O(n^2)
#space : O(n^2)

class Solution(object):
    def numIdenticalPairs(self, nums):
        dic_nums = {}
        for x in nums:
            if x in dic_nums:
                dic_nums[x] += 1
            else:
                dic_nums[x] = 1
        sum = 0
        for x in dic_nums:
            if dic_nums[x] == 1:
                continue
            sum += dic_nums[x]*(dic_nums[x] - 1)/2

        return sum
# 10 ms
# Time complexity: O(n)
# space complexity: O(n)

a = [1,2,3,1,1,3]
b = Solution()
result = b.numIdenticalPairs(a)
print(result)