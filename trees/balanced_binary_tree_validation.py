#determine if a binary tree is height-balanced,
# meaning no node's left subtree
#and right subtree have a height difference greater than 1.

#Height of the tree is equal to the depth of its deepest subtree, plus 1.
# Number of edges + 1


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


from typing import List

def create_node(root, nodes, i):
    if root == None:
        return

    if i < len(nodes) - 1:
        root.left = TreeNode(nodes[i+1])
    if i < len(nodes) - 2:
        root.right = TreeNode(nodes[i+2])

    i = i + 3
    create_node(root.left, nodes, i)
    create_node(root.right, nodes, i)

    return root

def create_tree(nodes: List[int]):
    i = 0
    root = TreeNode(nodes[i])
    return create_node(root, nodes, i)



def show_tree(root):
    if root == None:
        return

    print(root.val)

    show_tree(root.left)
    show_tree(root.right)

nodes = [5, 2, 7, 1, 4, None, 9, None, None, 3, None, 6, None]
root = create_tree(nodes)
print(show_tree(root))
