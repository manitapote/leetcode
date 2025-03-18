#invert a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#Stack implementation
def dfs(root: TreeNode):
    if root == None:
        return

    dfs(root.left)
    dfs(root.right)


#Queue implementation

from collections import deque
def bfs(root: TreeNode):
    queue = deque([root])
    while queue:
        root = queue.popleft()
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)


#dfs approach
def binary_tree_inversion(root: TreeNode):
    if root == None:
        return

    root.left, root.right = root.right, root.left

    binary_tree_inversion(root.left)
    binary_tree_inversion(root.right)

    return root

#bfs approach
def iterative_binary_tree(root: TreeNode):
    if root == None:
        return

    queue = deque([root])
    while queue:
        temp = queue.popleft()

        temp.left, temp.right = temp.right, temp.left

        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    return root




