from typing import List, Optional
class Solution:
    def findMaxAverage(self,
                       nums: List[int],
                       k: int
                       ) -> float:
        if len(nums) == 1:
            return nums[0]

        ans = s = sum(nums[:k])
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            ans = max(s, ans)

        return ans/k



#Reuse the sum of before


nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums, k))
