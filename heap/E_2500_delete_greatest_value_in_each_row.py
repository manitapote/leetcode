# 2500. Delete Greatest Value in Each Row
# You are given an m x n matrix grid consisting of positive integers.
# Perform the following operation until grid becomes empty:
# Delete the element with the greatest value from each row.
# If multiple such elements exist, delete any of them.
# Add the maximum of deleted elements to the answer.

# Note that the number of columns decreases by one after each operation.

# Return the answer after performing the operations described above.

# import heapq
# class Solution(object):
#     def deleteGreatestValue(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#
#         total = 0
#         while len(grid[0]) != 0:
#             answer = 0
#             for row in grid:
#                 largest = heapq.nlargest(1, row)
#                 row.remove(largest[0])
#                 # answer.append(largest[0])
#                 if answer < largest[0]:
#                     answer = largest[0]
#
#             total = total + answer
#
#         return total

#Best solution
#sorting the element first.
#each column are ascending or descending
#no need to remove elements
class Solution(object):
    def deleteGreatestValue(self, grid):
        for row in grid: row.sort()

        return sum(max(col) for col in zip(*grid))


grid = [[1,2,4],[3,3,1]]

object = Solution()
result = object.deleteGreatestValue(grid)

print(result)


grid = [[10]]
object = Solution()
result = object.deleteGreatestValue(grid)

print(result)
