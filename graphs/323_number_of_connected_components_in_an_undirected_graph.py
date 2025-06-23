# # 323. Number of Connected Components in an Undirected Graph
#
#
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
#
# Return the number of connected components in the graph.

from typing import List, Optional
from collections import defaultdict
from collections import deque
class Solution:
    def countComponents(self,
                        n: int,
                        edges: List[List[int]]
                        ) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        total = 0
        for i in range(n):
            if i in visited:
                continue

            queue = deque([i])

            while queue:
                node = queue.popleft()
                visited.add(node)

                for x in graph[node]:
                    if x in visited:
                        continue
                    queue.append(x)

            total  += 1

        return total


n = 5
edges = [[0,1],[1,2],[3,4]]
a = Solution()
print(a.countComponents(n, edges))
n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
print(a.countComponents(n, edges))



