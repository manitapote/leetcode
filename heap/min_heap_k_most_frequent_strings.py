from typing import List
from collections import Counter
import heapq
class Pair:
    def __init__(self, strs, freq):
        self.strs = strs
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.strs < other.strs

        return self.freq < other.freq

def k_most_frequent_strings(strs: List[str],
                            k: int
                            ):
    #O(n)
    hashmap = Counter(strs)
    min_heap = []

    #O(nlog(k))
    for key, item in hashmap.items():
        heapq.heappush(min_heap,
                       Pair(key, item)
                       )
        #O(nlog(k))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    #O(klog(k) + k)
    return [heapq.heappop(min_heap).strs for i in range(k)][::-1]

#Time complexity= O(klog(k) + k + nlog(k))
strs = ['go', 'coding','byte',
        'byte', 'go', 'interview',
        'interview', 'go'
        ]
k = 2
print(k_most_frequent_strings(strs, k))


