class Solution(object):
    #45ms
    #Time complexity : O(n)
    #Space complexity: O(n)
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums.extend(nums)
        # return nums
        #return nums + nums

        return nums*2

nums = [1,2,1]

a = Solution()
print(a.getConcatenation(nums))