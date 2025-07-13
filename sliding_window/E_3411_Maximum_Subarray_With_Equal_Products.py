import math
from typing import List
from math import gcd
class Solution:
    def maxLength(self,
                  nums: List[int]
                  ) -> int:
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)

        ans = 0
        for i, x in enumerate(nums):
            p = 1
            g = 0
            l = 1
            for j in range(i, len(nums)):
                p = p*nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if p == g * l:
                    ans = max(ans, j - i + 1)
        return ans

nums = [1, 2, 1, 2, 1, 1, 1]
print(Solution().maxLength(nums))


