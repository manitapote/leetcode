from typing import List
from collections import Counter
class Solution:
    def findLHS(self,
                nums: List[int]
                ) -> int:
        counts = Counter(nums)
        total = []
        for i, x in counts.items():
            if i+1 in counts:
                total.append(x+counts[i+1])

        return max(total) if total else 0




nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(Solution().findLHS(nums))
nums = [1,2,3,4]
print(Solution().findLHS(nums))
