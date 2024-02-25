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

import heapq
#25ms beats 90.99% :D
class Solution(object):
    def numberGame(self, nums):
        #O(nlog(n))
        # heapq.heapify(nums)

        #O(nlog(n)) as n times to pop and log(n) to heapify
        heap = heapq.nsmallest(len(nums), nums)

        index = len(heap) - 1
        i = 1
        while i <= index:
            heap[i], heap[i-1] = heap[i-1], heap[i]

            i = i + 2

        return heap


nums= [2,5,3,8]

result = Solution().numberGame(nums)
print(result)