#1791 Find Center of Star Graph

# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
#
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

from typing import List, Optional
class Solution:
    def findCenter(self,
                   edges: List[List[int]]
                   ) -> int:
        nodes = [0]*(len(edges) + 2)
        for i, j in edges:
            nodes[i] += 1
            nodes[j] += 1

        for i, x in enumerate(nodes):
            if x == len(edges):
                return i


edges = [[1,2],[2,3],[4,2]]
a = Solution()
print(a.findCenter(edges))
edges = [[1,2],[5,1],[1,3],[1,4]]
print(a.findCenter(edges))

