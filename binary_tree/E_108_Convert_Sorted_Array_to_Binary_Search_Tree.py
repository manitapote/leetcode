# Definition for a binary tree node.
class TreeNode:
    def __init__(self,
                 val=0,
                 left=None,
                 right=None
                 ):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional
class Solution:
    def sortedArrayToBST(self,
                         nums: List[int]
                         ) -> Optional[TreeNode]:
        def dfs(left, right, nums):
            if left > right:
                return None

            mid = (left + right) // 2

            return TreeNode(nums[mid],
                            dfs(left, mid - 1, nums),
                            dfs(mid + 1, right, nums)
                            )
        return dfs(0, len(nums) -1, nums)



nums = [-10,-3,0,5,9]
print(Solution().sortedArrayToBST(nums).val)

