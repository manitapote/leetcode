#156 Binary tree upside down

# Given the root of a binary tree, turn the tree upside down and return the new root.

# You can turn a binary tree upside down with the following steps:
#
# The original left child becomes the new root.
# The original root becomes the new right child.
# The original right child becomes the new left child

# The mentioned steps are done level by level. It is guaranteed that every right node has a sibling
# (a left node with the same parent) and has no children.


# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = [1,2,3,4,5]
a_1 = TreeNode(1)
a_2 = TreeNode(2)
a_3 = TreeNode(3)
a_4 = TreeNode(4)
a_5 = TreeNode(5)

a_1.left = a_2
a_1.right = a_3
a_2.left = a_4
a_2.right = a_5
class Solution:
    def upsideDownBinaryTree(self,
                             root: Optional[TreeNode]
                             ) -> Optional[TreeNode]:

        temp = TreeNode(root.val)
        temp.


