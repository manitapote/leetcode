from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self,
                     nums: List[int],
                     k: int
                     ) -> List[int]:
        counts = Counter(nums)

        heap = [(-freq, index) for index, freq in counts.items()]

        heapq.heapify(heap)

        if len(heap) == 1:
            return [heapq.heappop(heap)[1]]

        i = 0
        result = []
        while i < k:
            result.append(heapq.heappop(heap)[1])
            i += 1

        return result

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
nums = [1]
k = 1
print(Solution().topKFrequent(nums, k))