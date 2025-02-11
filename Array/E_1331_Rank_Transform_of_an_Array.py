# #1331 Rank Transform of an Array
# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
import copy


# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.
# import copy
# class Solution:
#     def arrayRankTransform(self, arr):
#         bb = copy.deepcopy(arr)
#         arr.sort()
#         left = 0
#         rank = {}
#         dis = 1
#         while left < len(arr):
#             while left < (len(arr) - 1) and arr[left] == arr[left+1]:
#                 left = left + 1
#
#             rank[arr[left]] = dis
#             left = left + 1
#
#             dis += 1
#
#         result = []
#         for x in bb:
#             result.append(rank[x])
#
#         return result

import copy
class Solution:
    def arrayRankTransform(self, arr):
        arr_set = sorted(set(arr))
        track = {x: i+1 for i, x in enumerate(arr_set)}

        return [track[x] for x in arr]






arr = [40, 10, 20, 30]

a = Solution()
print(a.arrayRankTransform(arr))

arr = [100,100,100]
a = Solution()
print(a.arrayRankTransform(arr))

# arr = [37,12,28,9,100,56,80,5,12]
# a = Solution()
# print(a.arrayRankTransform(arr))