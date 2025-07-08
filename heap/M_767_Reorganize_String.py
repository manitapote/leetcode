#767 Reorganize String


from collections import Counter
import heapq
class Solution:
    def reorganizeString(self,
                         s: str
                         ) -> str:
        counts = Counter(s)
        heap = [(-freq, index) for index, freq in counts.items()] #O(n)

        heapq.heapify(heap) #O(n)

        result = ''
        while heap: #O(n*max(freq))
            freq, x = heapq.heappop(heap) #O(log(n))

            result += x

            if freq + 1 < 0:
                heap.append((freq+1, x))

            if len(heap) == 1 and heap[0][0] < 1 and heap[0][1] == result[-1]:
                return ''

        return result

s = 'aab'
print(Solution().reorganizeString(s))
s = 'aaab'
print(Solution().reorganizeString(s))