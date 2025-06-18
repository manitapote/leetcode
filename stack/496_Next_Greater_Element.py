# 496 Next Greate Element

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

def nextGreaterElement(nums1, nums2):
    nextGreater = {x: -1 for x in nums1}
    stack = []

    for i, x in enumerate(nums2):
        while stack and nums2[stack[-1]] < x:
            idx = stack.pop()
            if nums2[idx] in nextGreater:
                nextGreater[nums2[idx]] = x

        stack.append(i)

    result = []
    for x in nums1:
        if x in nextGreater:
            result.append(nextGreater[x])

    return result




nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nums1)
print(nums2)
print(nextGreaterElement(nums1, nums2))

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))
