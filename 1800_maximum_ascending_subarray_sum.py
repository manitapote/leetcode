class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_track = 0
        total = 0
        nums.insert(0, 0)
        for i in range(len(nums)):
            if nums[i-1] <= nums[i]:
                total = total + nums[i-1]
            else:
                if max_track < total:
                    max_track = total
                total = 0


        return max_track



# nums = [10,20,30,5,10,50, 4000]
nums = [10,20,30,5,10,50]

# nums =  [10000, 10,20,30000000,5,10,50000]
#cases [1, 20,20,.. 10000]
#cases [1,23, 10000, 2,3]

a = Solution()
print(a.maxAscendingSum(nums))
