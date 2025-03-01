# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
#
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

#
# Return the minimum possible difference.

class Solution:
    def minimumDifference(self, nums, k):
        #sort, find difference
        if len(nums) == 1:
            return 0

        nums.sort()

        return min([nums[i+k-1] - nums[i] for i in range(len(nums) - k + 1)])




nums=[90]
k=1
print(Solution().minimumDifference(nums,k))

nums=[9,4,1,7]
k=2
print(Solution().minimumDifference(nums,k))


nums=[87063, 61094, 44530, 21297, 95857, 93551, 9918]
k=6
print(Solution().minimumDifference(nums,k))