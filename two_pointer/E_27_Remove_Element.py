from typing import List
class Solution:
    def removeElement(self,
                      nums: List[int],
                      val: int
                      ) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and val == nums[0]:
            return 0

        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l, nums

#
#
# nums = [3,2,2,3]
# val = 3
# print(Solution().removeElement(nums, val))
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# print(Solution().removeElement(nums, val))
nums = [4, 5]
val = 4
print(Solution().removeElement(nums, val))
