# You are given a 0-indexed integer array nums of even length and there is also
# an empty array arr. Alice and Bob decided to play a game where in every round
# Alice and Bob will do one move. The rules of the game are as follows:
#
# Every round, first Alice will remove the minimum element from nums,
# and then Bob does the same.
# Now, first Bob will append the removed element in the array arr,
# and then Alice does the same.
# The game continues until nums becomes empty.
# Return the resulting array arr.

import math

class Solution(object):
    def numberGame(self, nums):
        #create heap, separate function for each index
        #delete elment from heap
        heap = self.min_heap(nums)
        sorted_data = self.delete(heap)
        ordered_data = self.reorder(sorted_data)

        return ordered_data

    #O(n)
    #pop has to shift the elements so this is not efficient, makes it O(n^2)
    def reorder(self, heap):
        # ordered = []
        # while len(heap) > 0:
        #     a, b = heap.pop(0), heap.pop(0)
        #
        #     ordered.append(b)
        #     ordered.append(a)

        for i in range(1, len(heap), 2):
            heap[i], heap[i-1] = heap[i-1], heap[i]

        return heap

    #O(nlog(n))
    def min_heap(self, nums):
        heap = []
        for num in nums:
            heap.append(num)
            index = len( heap) - 1
            # parent = i/2 but here index starts at 0 so has to adjust
            heap = self.heapify(index, heap)
        return  heap

    #O(log(n))
    def heapify(self, index, heap):
        while index > 0 and heap[(index - 1) // 2] > heap[index]:
            heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
            index = (index - 1) // 2

        return heap

    #O(nlog(n))
    def delete(self, heap):
        sorted_data = []
        index = len(heap) - 1

        while index >= 0:
            root = heap[0]
            heap[0] = heap[index]

            heap.pop(index)
            index = len(heap) - 1
            heap = self.heapify(index, heap)

            sorted_data.append(root)

        return sorted_data

nums= [2,5,3,8]

result = Solution().numberGame(nums)
print(result)