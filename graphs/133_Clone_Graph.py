# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
# """


class Node:
    def __init__(self, val = 0,
                 neighbors = None
                 ):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.nodes = {}

    #T=O(n+e)
    #S=O(n)
    def dfs(self, root):
        if root.val in self.nodes:
            return self.nodes[root.val]

        new_node = Node(root.val)
        self.nodes[root.val] = new_node

        for neighbor in root.neighbors:
            new_neighbor = self.dfs(neighbor)
            new_node.neighbors.append(new_neighbor)

        return new_node



adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
a_1 = Node(1)
a_2 = Node(2)
a_3 = Node(3)
a_4 = Node(4)

a_1.neighbors = [a_2, a_4]
a_2.neighbors = [a_1, a_3]
a_3.neighbors = [a_2, a_4]
a_4.neighbors = [a_1, a_3]

a = Solution()
root = a.dfs(a_1)
print(root)


def dfs(root, visited):
    visited.add(root)
    print(root.val)

    for x in root.neighbors:
        if x not in visited:
            dfs(x, visited)


visited =  set()
dfs(root, visited)