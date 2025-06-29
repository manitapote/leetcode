# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
class TreeNode:54
    def __init__(self,
                 val=0,
                 left=None,
                 right=None
                 ):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self,
                             root: Optional[TreeNode]
                             ) -> int:

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        dfs(root)

        return self.ans









root = [1, 2, 3, 4, 5]

a_1 = TreeNode(1)
a_2 = TreeNode(2)
a_3 = TreeNode(3)
a_4 = TreeNode(4)
a_5 = TreeNode(5)

a_1.left = a_2
a_1.right = a_3
a_2.left = a_4
a_2.right = a_5

a = Solution()
print(a.diameterOfBinaryTree(a_1))

root = [1,2]
a_1 = TreeNode(1)
a_2 = TreeNode(2)
a_1.left = a_2

a = Solution()
print(a.diameterOfBinaryTree(a_1))

#Time complexity: O(n)
#Space complexity: O(h) #height of the stack



