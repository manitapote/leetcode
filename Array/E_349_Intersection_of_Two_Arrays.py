# #349 Intersection of two arrays
# Given two integer arrays nums1 and nums2, return an array of their
# intersection
# . Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(set(nums1).intersection(set(nums2))))

#Time complexity: O(N1), O(N2) for converting list to set,
#O(intersection(N1, N2)) for
#O(N1+N2) max for converting set to list
#final complexity = O(N1+N2)

# class Solution:
#     def intersection(self, nums1, nums2):
#         nums2.sort()
#         nums1.sort()
#
#         result = set()
#
#         for i in range(max(len(nums1), len(nums2))):
#             if i < len(nums1) and nums1[i] in nums2 and nums1[i] not in result:
#                 result.add(nums1[i])
#             if i < len(nums2) and nums2[i] in nums1 and nums2[i] not in result:
#                 result.add(nums2[i])
#
#         return list(result)

#Time complexity log(N)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersection(nums1, nums2))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersection(nums1, nums2))
