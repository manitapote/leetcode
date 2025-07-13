from typing import List
class Solution:
    def minimumSumSubarray(self,
                           nums: List[int],
                           l: int,
                           r: int
                           ) -> int:
        if len(nums) == 0:
            return -1

        ans = float('inf')
        for i in range(l, r+1):
            total = sum(nums[:i])
            if total > 0:
                ans = min(ans, total)

            new_total = total
            for j in range(1, len(nums) - i + 1):
                new_total += nums[j+i-1] - nums[j-1]
                if new_total > 0:
                    ans = min(ans, new_total)

        return ans if ans != float('inf') else -1


nums = [3, -2, 1, 4]
l = 2
r = 3
print(Solution().minimumSumSubarray(nums, l, r))

nums = [-2, 2, -3, 1]
l = 2
r = 3
print(Solution().minimumSumSubarray(nums, l, r))

nums = [1, 2, 3, 4]
l = 2
r = 4
print(Solution().minimumSumSubarray(nums, l, r))

nums = [-12, 8]
l = 1
r = 1
print(Solution().minimumSumSubarray(nums, l, r))
