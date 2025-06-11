#94 Binary Tree Inorder Traversal

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



a_1 = TreeNode(1)
a_2 = TreeNode(2)
a_1.right = a_2
a_3 = TreeNode(3)
a_2.left = a_3

def inorder_traversal(root):
    result = []
    def dfs(root, result):
        if not root:
            return

        dfs(root.left, result)
        result.append(root.val)
        dfs(root.right, result)


    dfs(root, result)

    return result

print(inorder_traversal(a_1))


a_1 = TreeNode(1)
a_2 = TreeNode(2)
a_3 = TreeNode(3)
a_4 = TreeNode(4)
a_5 = TreeNode(5)
a_6 = TreeNode(6)
a_7 = TreeNode(7)
a_8 = TreeNode(8)
a_9 = TreeNode(9)

a_1.left = a_2
a_1.right = a_3
a_2.left = a_4
a_2.right = a_5
a_5.left = a_6
a_5.right = a_7
a_3.right = a_8
a_8.left = a_9

print(inorder_traversal(a_1))

print(inorder_traversal(None))