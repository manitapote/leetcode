from typing import List
class Solution:
    def intersect(self,
                  nums1: List[int],
                  nums2: List[int]
                  ) -> List[int]:
        i = 0
        result = []
        nums1.sort()
        nums2.sort()
        if len(nums1) > len(nums2):
            largest = nums1
            smallest = nums2
        else:
            largest = nums2
            smallest = nums1
        j = 0
        while i < len(smallest) or j < len(largest):
            if i > len(smallest) - 1:
                return result
            if j > len(largest) - 1:
                return result

            if smallest[i] == largest[j]:
                result.append(smallest[i])

                i += 1
                j += 1
            elif smallest[i] < largest[j]:
                i += 1
            else:
                j += 1

        return result


nums1 = [1, 1, 2, 2]
nums2 = [2, 2]
print(Solution().intersect(nums1, nums2))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersect(nums1, nums2))
nums1 = [2, 1]
nums2 = [1, 1]
print(Solution().intersect(nums1, nums2))


#To apply two pointer, need some logical order
#If not present would logical order help.
