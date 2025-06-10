# 94 Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a_5 = TreeNode(5)
a_1 = TreeNode(1)
a_8 = TreeNode(8)
a_7 = TreeNode(7)
a_6 = TreeNode(6)
a_4 = TreeNode(4)
a_5.left = a_1
a_5.right = a_8
a_1.left = a_7
a_1.right = a_6
a_8.right = a_4


b_1 = TreeNode(1)
b_2 = TreeNode(2)
b_3 = TreeNode(3)
b_1.right = b_2
b_2.left = b_3

def read(node: TreeNode):
    if node == None:
        return
    print(node.val)
    read(node.left)
    read(node.right)

print('\n\n')
# read(a_5)


def inorder_traversal(root: TreeNode):
    if not root:
        return

    inorder_traversal(root.left)
    process(root)
    inorder_traversal(root.right)

def process(root: TreeNode):
    print(root.val)



c_1 = TreeNode(1)
c_2 = TreeNode(2)
c_3 = TreeNode(3)
c_4 = TreeNode(4)
c_5 = TreeNode(5)
c_6 = TreeNode(6)
c_7 = TreeNode(7)
c_8 = TreeNode(8)
c_9 = TreeNode(9)

c_1.left = c_2
c_1.right = c_3
c_2.left = c_4
c_2.right = c_5
c_5.left = c_6
c_5.right = c_7
c_3.right = c_8
c_8.left = c_9


# inorder_traversal(b_1)
d_1 = TreeNode(1)
inorder_traversal(d_1)