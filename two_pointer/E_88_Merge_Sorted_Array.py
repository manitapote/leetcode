class Solution:
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return nums1
        if n == 0:
            return nums1
        n1 = m - 1
        n2 = n - 1
        total = len(nums1) - 1

        while n1 >=0 and n2 >= 0:
            if nums1[n1] > nums2[n2]:
                nums1[total] = nums1[n1]
                n1 -= 1
            else:
                nums1[total] = nums2[n2]
                n2 -= 1

            total -= 1

        while n2 >= 0:
            nums1[total] = nums2[n2]
            n2 -= 1
            total -= 1

        return nums1




nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
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
nums1 = [2,0]
m=1
nums2=[1]
n = 1
print(Solution().merge(nums1, m, nums2, n))