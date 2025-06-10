#104 Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to
# the farthest leaf node.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a_3 = TreeNode(3)
a_9 = TreeNode(9)
a_20 = TreeNode(20)
a_15 = TreeNode(15)
a_7 = TreeNode(7)

a_3.left = a_9
a_3.right = a_20
a_20.left = a_15
a_20.right = a_7

def height(root: TreeNode):
    if root == None:
        return 0

    left_h = height(root.left)
    right_h = height(root.right)

    return 1 + max(left_h, right_h)


# print(height(a_3))

b_1 = TreeNode(1)
b_2 = TreeNode(2)
b_1.right = b_2

c_1 = TreeNode(1)

# print(height(b_1))
print(height(c_1))
