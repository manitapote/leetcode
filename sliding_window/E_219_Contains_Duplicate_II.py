from typing import List
from collections import defaultdict
# class Solution:
#     def containsNearbyDuplicate(self,
#                                 nums: List[int],
#                                 k: int
#                                 ) -> bool:
#         hashmap = defaultdict(int)
#         for i, x in enumerate(nums):
#             if x in hashmap and abs(i - hashmap[x]) <= k:
#                 return True
#             hashmap[x] = i
#
#         return False

class Solution:
    def containsNearbyDuplicate(self,
                                nums: List[int],
                                k: int
                                ) -> bool:
        for i, x in enumerate(nums):
            if x in nums[i+1:i+k+1]:
                return True

        return False

#look up in longer list can be tricky
nums = [1, 2, 3, 1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))
nums = [1, 0, 1, 1]
k = 1
print(Solution().containsNearbyDuplicate(nums, k))
nums = [1, 2, 3, 1, 2, 3]
k = 2
print(Solution().containsNearbyDuplicate(nums, k))




