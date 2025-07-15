# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def sortedArrayToBST(self,
                         nums: List[int]
                         ) -> Optional[TreeNode]:
        if len(nums) == 0:
            return TreeNode(None)
        def dfs(nums):
            if len(nums) == 0:
                return TreeNode(None)

            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            root.left = dfs(nums[:mid])
            root.right = dfs(nums[mid+1:])

            return root

        return dfs(nums)




#
#
# nums = [1, 3]
# root = Solution().sortedArrayToBST(nums)
# while root:
#     print(root.val)
#     print(root.left.v)
nums = [-10,-3,0,5,9]
root = Solution().sortedArrayToBST(nums)
print(root.val, root.left.val, root.right.val, root.left.left.val,
      root.left.right.val, root.right.left.val, root.right.right.val
      )