#144 Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a_1 = TreeNode(1)
a_2 = TreeNode(2)
a_3 = TreeNode(3)

a_1.right = a_2
a_2.left = a_3

def preorder(root: TreeNode, order) -> TreeNode:
    if not root:
        return None
    process(root, order)
    preorder(root.left, order)
    preorder(root.right, order)

def process(root:TreeNode, order) -> None:
    print(root.val)
    order.append(root.val)

# preorder(a_1)

b_1 = TreeNode(1)
b_2 = TreeNode(2)
b_3 = TreeNode(3)
b_4 = TreeNode(4)
b_5 = TreeNode(5)
b_6 = TreeNode(6)
b_7 = TreeNode(7)
b_8 = TreeNode(8)
b_9 = TreeNode(9)

b_1.left = b_2
b_2.left = b_4
b_2.right = b_5
b_5.left = b_6
b_5.right = b_7

b_1.right = b_3
b_3.right = b_8
b_8.left = b_9

order = []
preorder(b_1, order)
print(order)


