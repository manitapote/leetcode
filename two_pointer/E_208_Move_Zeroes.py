class Solution:
    def moveZeroes(self, nums):
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return nums

        l = 0
        r = 0
        while r < len(nums):
            if nums[r] == 0:
                l = r
            while nums[r] == 0:
                r += 1
            nums[l] = nums[r]
            nums[r] = 0
            r += 1

        return nums
nums = [1,0, 2, 0 , 12]
nums = [0,1,0,3,12]
nums = [0]