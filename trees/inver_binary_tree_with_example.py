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


def dfs(node: TreeNode):
    if node == None:
        return
    node.left, node.right = node.right, node.left
    dfs(node.left)
    dfs(node.right)

    print(node.val)

    return node



# dfs(a_5)
def with_stack(node: TreeNode):
    stack = []
    stack.append(node)

    while stack:
        root = stack.pop()
        root.left, root.right = root.right, root.left

        if root.left:
            stack.append(root.left)

        if root.right:
            stack.append(root.right)

    return node

with_stack(a_5)
def read(node: TreeNode):
    if node == None:
        return
    print(node.val)
    read(node.left)
    read(node.right)

print('\n\n')
read(a_5)


#It is useful to use a stack instead of dfs recursive tree if the height of the tree is very large.
#It is set to 1000 at default.
