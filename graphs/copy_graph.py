"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
# """


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional, Dict

from queue import deque
class Solution:
    def dfs(self, node: Node, visited: Dict[Node, Node]):
        if node in visited:
            return visited[node]

        new_node = Node(node.val)
        visited[node] = new_node
        for n in node.neighbors:
            new_neigh = self.dfs(n, visited)
            new_node.neighbors.append(new_neigh)

        return new_node

    def bfs(self, node: Node):
        mapping = {}
        queue = deque([node])
        mapping[node] = Node(node.val)
        while queue:
            root = queue.popleft()

            for n in root.neighbors:
                if n not in mapping:
                    mapping[n] = Node(n.val)
                    queue.append(mapping[n])

                mapping[root].neighbors.append(mapping[n])

        return node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        # return self.dfs(node, {})
