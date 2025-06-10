## 222 Count Complete Tree Nodes

# Given the root of a complete binary tree, return the number of the nodes in the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Design an algorithm that runs in less than O(n) time complexity.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




a_1 = TreeNode(1)
a_2 = TreeNode(2)
a_3 = TreeNode(3)
a_4 = TreeNode(4)
a_5 = TreeNode(5)
a_6 = TreeNode(6)

a_1.left = a_2
a_1.right = a_3
a_2.left = a_4
a_2.right = a_5
a_3.left = a_6

def count_nodes(root: TreeNode) -> int:
    def dfs(root: TreeNode) -> int:
        if not root:
            return 0

        count_l = dfs(root.left)
        count_r = dfs(root.right)

        return 1 + count_l + count_r

    return dfs(root)

print(count_nodes(a_1))