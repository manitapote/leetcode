# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def maxDepth(self,
                 root: Optional[TreeNode]
                 ) -> int:

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            return 1 + max(left, right)

        return dfs(root) + 1

root = [3, 9, 20, None, None, 15, 7]

a_3 = TreeNode(3)
a_3.left = TreeNode(9)
a_20 = TreeNode(20)
a_15 = TreeNode(15)
a_7 = TreeNode(7)
a_20.left = a_15
a_20.right = a_7


print(Solution().maxDepth(a_3))
