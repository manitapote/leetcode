from typing import List
from collections import defaultdict
class Solution:
    def longestOnes(self,
                    nums: List[int],
                    k: int
                    ) -> int:
        l = 0
        total0 = 0
        ans = float('-inf')
        for r, val in enumerate(nums):
            if val == 0:
                total0 += 1

            while total0 > k:
                if nums[l] == 0:
                    total0 -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(Solution().longestOnes(nums, k))
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(Solution().longestOnes(nums, k))
