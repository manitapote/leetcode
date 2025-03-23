# 257. Binary Tree Paths
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children

#Binary Tree height:
#Left child : 2n + 1
#Right Child: 2n + 2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.right = TreeNode(5)

def dfs(root, candidate, result):
    if root == None:
        return

    candidate.append(root.val)

    if root.left == None and root.right == None:
        result.append(candidate[:])
    else:

        dfs(root.left, candidate, result)
        dfs(root.right, candidate, result)

    candidate.pop()


#1->2->4, 1->2->5, 1->3
def find_path(root):
    result = []
    dfs(root, [], result)

    return result


print(find_path(root))


# class Solution:
#     def binaryTreePaths(self, root):
#         def dfs(node, path, result):
#             if not node:
#                 return
#             path.append(node.val)
#             # print(path)
#             if not node.left and not node.right:
#                 result.append(path)
#             else:
#                 dfs(node.left, path+'->', result)
#                 dfs(node.right, path +'->', result)
#
#         result = []
#         dfs(root, [], result)
#         return result


# from typing import Optional, List
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         def dfs(root: Optional[TreeNode]):
#             if root is None:
#                 return
#             t.append(str(root.val))
#             if root.left is None and root.right is None:
#                 ans.append("->".join(t))
#             else:
#                 dfs(root.left)
#                 dfs(root.right)
#             t.pop()
#
#         ans = []
#         t = []
#         dfs(root)
#         return ans



# print(Solution().binaryTreePaths(root))