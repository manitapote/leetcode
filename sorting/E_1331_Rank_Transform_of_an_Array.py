#1331 Rank Transform of an Array

# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

#list search is O(n) time complexity
class Solution:
    def arrayRankTransform(self, arr):
        test = list(sorted(set(arr)))
        track = {x: i+1 for i, x in enumerate(test)}

        return [track[x] for x in arr]



arr = [40, 10, 20, 30]
print(Solution().arrayRankTransform(arr))

arr = [100,100,100]
print(Solution().arrayRankTransform(arr))