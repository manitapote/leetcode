# #1200 Minimum Absolute Difference
#
# #Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
#
#
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr


class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        left = 0
        result = []

        while left < len(arr) - 1:
            diff = abs(arr[left+1] - arr[left])
            if min_diff > diff:
                min_diff = diff
                result = [[arr[left], arr[left+1]]]
            elif min_diff == diff:
                result.append([arr[left], arr[left+1]])

            left += 1

        return result




# arr = [4, 2, 1, 3]
# print(Solution().minimumAbsDifference(arr))
# arr = [1,3,6,10,15]
# print(Solution().minimumAbsDifference(arr))
# arr = [3,8,-10,23,19,-4,-14,27]
# print(Solution().minimumAbsDifference(arr))
# arr = [40,11,26,27,-20]
# print(Solution().minimumAbsDifference(arr))
arr = [3,8,-10,23,19,-4,-14,27]
print(Solution().minimumAbsDifference(arr))
