# There is a bi-directional
# graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
#
# You want to determine if there is a
# valid path that exists from vertex source to vertex destination.
#
# Given edges and the integers n, source,
# and destination, return true if there is a valid path from source to destination, or false otherwise.

from typing import List
from collections import defaultdict
class Solution:
    def validPath(self,
                  n: int,
                  edges: List[List[int]],
                  source: int,
                  destination: int
                  ) -> bool:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            if node == destination:
                return True

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False

        visited = set()
        return dfs(source)

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

a = Solution()
print(a.validPath(n, edges, source, destination))