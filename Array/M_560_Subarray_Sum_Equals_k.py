class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count =0
        prefix_dict = {0:1}
        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            if diff in prefix_dict:
                count += prefix_dict[diff]

            prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1

        return count


nums = [1, 2, 3]
k = 3
print(Solution().subarraySum(nums, k))
nums = [1,1,1]
k = 2
print(Solution().subarraySum(nums, k))


