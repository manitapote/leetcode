from typing import List
from collections import defaultdict
class Solution:
    def longestOnes(self,
                    nums: List[int],
                    k: int
                    ) -> int:
        hashmap = defaultdict(int)
        left = 0
        l = 1
        total = 0
        for i, val in enumerate(nums):
            # while l < k and val == 0:
            #     total = max(total, i - left + 1)
            #     l += 1
            # left = i+1
            #
            # if l >= k:
            #     l = 0


        return total

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(Solution().longestOnes(nums, k))
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(Solution().longestOnes(nums, k))
