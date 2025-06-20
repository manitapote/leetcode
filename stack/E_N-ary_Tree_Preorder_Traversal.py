#589 N-ary Tree Preorder Traversal

# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

from typing import Optional, List
class Node:
    def __init__(self,
                 val: Optional[int] = None,
                 children: Optional[List['Node']] = None
                 ):
        self.val = val
        self.children = children


a_1 = Node(1)
a_2 = Node(2)
a_3 = Node(3)
a_4 = Node(4)
a_5 = Node(5)
a_6 = Node(6)

a_3.children = [a_5, a_6]
a_1.children = [a_3, a_2, a_4]


class Solution:
    def preorder(self, root: Node) -> List[int]:

        result = []
        def dfs(root: Node):
            if not root:
                return

            result.append(root.val)

            if root.children:
                for child in root.children:
                    dfs(child)

        dfs(root)

        return result


a = Solution()
print(a.preorder(a_1))



