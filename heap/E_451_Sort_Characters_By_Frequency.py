#451 Sort Characters By Frequency
from collections import Counter
import heapq
class Solution:
    def frequencySort(self,
                      s: str
                      ) -> str:
        counts = Counter(s)
        heap = [(-freq, index) for index, freq in counts.items()]

        heapq.heapify(heap) #O(n)
        result = ''
        while heap:
            freq, character = heapq.heappop(heap) #O(log(n))
            result += character*(-freq)

        return result


s = 'tree'
print(Solution().frequencySort(s))
s = "cccaaa"
print(Solution().frequencySort(s))
