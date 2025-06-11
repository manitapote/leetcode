#108 Convert sorted Array to Binary Search Tree

# Given an integer array nums where the elements are sorted in
# ascending order, convert it to a height-balanced binary search tree.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def dfs(left, right, nums):
        if left > right:
            return None

        mid = (left + right) // 2


        return TreeNode(nums[mid],
                        dfs(left, mid - 1, nums),
                        dfs(mid + 1, right, nums)
                        )

    return dfs(0, len(nums) - 1, nums)



nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)

#Time complexity:
#create one node = O(1)
#dfs on two halves = n/2
#T(n) = T(n/2) + T(n/2) + O(1) = O(n)


#Space complexity
#Recursion stack depth is based on the height of the tree.
#Balanced BST, height is: O(log(n)) (recursion stack)


result = []
def read(node: TreeNode, result):
    if node == None:
        result.append(None)
        return

    read(node.left, result)
    result.append(node.val)
    read(node.right, result)



print('\n\n')
read(root, result)
print(result)
# nums = [1,3]