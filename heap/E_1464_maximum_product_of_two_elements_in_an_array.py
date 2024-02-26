# 1464. Maximum Product of Two Elements in an Array

# Given the array of integers nums, you will choose two different indices i and j of
# that array. Return the maximum value of (nums[i]-1)*(nums[j]-1)
# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0),
# you will get the maximum value,
# that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

import heapq

#Steps : heapify and deletion
# O(nlog(n)) => heapify once after root is deleted
#O(n) for heapify for best optimized code
class Solution(object):
    def maxProduct(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        max_2 = heapq.nlargest(2, nums)

        return (max_2[0]-1)*(max_2[1]-1)

nums = [1,5,4,5]
a = Solution()
result = a.maxProduct(nums)
print(result)