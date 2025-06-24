# #207 Course Schedule
#
#
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#

from typing import List
from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self,
                  numCourses: int,
                  prerequisites: List[List[int]]
                  ) -> bool:
        graph = defaultdict(list)
        in_degree = [0]*numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        queue = deque([i for i, x in enumerate(in_degree) if x==0])
        total = 0
        while queue:
            node = queue.pop()
            total += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return total == numCourses

numCourses = 2
prerequisites = [[1,0]]
a = Solution()
print(a.canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(a.canFinish(numCourses, prerequisites))
