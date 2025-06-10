#E 100 Same tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a_1 = TreeNode(1)
a_2 = TreeNode(2)
a_3 = TreeNode(3)
a_1.left = a_2
a_1.right = a_3

b_1 = TreeNode(1)
b_2 = TreeNode(2)
b_3 = TreeNode(3)
b_1.left = b_2
b_1.right = b_3


def same(root1: TreeNode, root2: TreeNode) -> bool:
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.val != root2.val:
        return False

    # flag1 = same(root1.left, root2.left)
    # flag2 = same(root1.right, root2.right)

    return same(root1.left, root2.left) and same(root1.right, root2.right)

# print(same(a_1, b_1))

c_1 = TreeNode(1)
c_2 = TreeNode(2)
c_1.left = c_2

d_1 = TreeNode(1)
d_2 = TreeNode(2)
d_1.right = d_2

print(same(c_1, d_1))

a_1 = TreeNode(1)
a_2 = TreeNode(2)
a_3 = TreeNode(3)
a_1.left = a_2
a_1.right = a_3

b_1 = TreeNode(1)
b_2 = TreeNode(2)
b_3 = TreeNode(3)
b_1.left = b_3
b_1.right = b_2

print(same(a_1, b_1))