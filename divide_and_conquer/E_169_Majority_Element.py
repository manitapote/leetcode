class Solution:
    def majorityElement(self,
                        nums
                        ):
        def dfs(l, r):
            #base case when one element remaining in list
            if l == r:
                return nums[l]

            #divide
            mid = (l + r)//2
            left = dfs(l, mid)
            right = dfs(mid+1, r)
            print('left: ', left, 'right: ', right)

            if left == right:
                return left

            #count numbers
            left_count = sum([1 for i in range(l, r+1) if nums[i] == left])
            right_count = sum([1 for i in range(l, r+1) if nums[i] == right])

            print(left, left_count, right, right_count)

            return left if left_count > right_count else right

        return dfs(0, len(nums) - 1)


class Solution:
    def majorityElement(self,
                        nums
                        ):

        nums.sort()

        return nums[len(nums)//2]

nums = [3, 2, 3]
print(Solution().majorityElement(nums))
nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))
