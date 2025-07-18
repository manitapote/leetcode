#1762 Buildings With an Ocean View

# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
#
# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.
#
# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

from typing import List, Optional
# class Solution:
#     def findBuildings(self,
#                       heights: List[int]
#                       ) -> List[int]:
#
#         stack = []
#         for i, x in enumerate(heights):
#             while stack and heights[stack[-1]] < x:
#                 stack.pop()
#
#             stack.append(i)
#
#         return stack

#Time = O(n^2)

class Solution:
    def findBuildings(self,
                      heights: List[int]
                      ) -> List[int]:

        result = []
        max_height = -1
        for i in range(len(heights) -1 , -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]

                result.append(i)

        result.reverse()

        return result

#O(n)

heights = [4, 2, 3, 1]
a = Solution()
print(a.findBuildings(heights))

heights = [4,3,2,1]
print(a.findBuildings(heights))
