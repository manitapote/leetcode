# #88 Merge Sorted Array
#
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[m:] = nums2
#         nums1.sort()
#
#         return nums1

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m -1
        p2 = n -1
        last = m+n-1
        while p1 > -1 and p2 > -1:
            if nums1[p1] >= nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            else:
                nums1[last] = nums2[p2]
                p2 -= 1

            last -= 1

        while p2 >= 0:
            nums1[last] = nums2[p2]
            last -= 1
            p2 -= 1
        return nums1


nums1 = [1,2,3,0,0,0,0]
m = 3
nums2 = [0,2,5,6]
n = 4
print(Solution().merge(nums1, m, nums2, n))

nums1 = [0,0,0]
m = 0
nums2 = [2,5,6]
n = 3
print(Solution().merge(nums1, m, nums2, n))

nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
print(Solution().merge(nums1, m, nums2, n))

nums1 = [1,2,3,8,0,0,0, 0, 0, 0]
m = 4
nums2 = [2,5,6,7,8,9]
n = 6
print(Solution().merge(nums1, m, nums2, n))


nums1 = [1]
m = 1
nums2 = []
n = 0
print(Solution().merge(nums1, m, nums2, n))

nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(Solution().merge(nums1, m, nums2, n))