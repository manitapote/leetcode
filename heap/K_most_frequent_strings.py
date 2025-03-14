import heapq
from typing import List
from collections import Counter
# def k_most_frequent_strings_max_heap(strs: List[str],
#                                      k: int
#                                      ):
#     heap = []
#     #O(n)
#     hashmap = Counter(strs)
#     #O(nlog(n))
#     for key, val in hashmap.items():
#         heapq.heappush(heap, (-val, key))
#
#     result = []
#     #O(klog(m))
#     for i in range(k):
#         freq, item = heapq.heappop(heap)
#         result.append(item)
#
#     return result

#Total time complexity: O(n) + O(mlog(m)) + O(klog(m))
#Worst case: m=n, O(n+nlog(n)+ klog(n)) = O(nlog(n) + klog(n))
#Problem is we are heapifying everytime we push, if there is a
#way to heapify once, after all the elements have been in the list

# def  k_most_frequent_strings_max_heap(strs: List[str],
#                                       k: int
#                                       ):
#     hashmap = Counter(strs)
#     hashmap = sorted(hashmap.items(), key=lambda x: (x[1], x[0]),
#                      reverse=True
#                      )
#     result = []
#     for i, (key, val) in enumerate(hashmap):
#         if i >= k:
#             return result
#         result.append(key)

##This method does not work because if the frequencies are equal,
##it has to be in ascending order by lexical characters

#Time complexity: O(n) + O(mlog(m)) + O(k) = O(nlog(n))

class Pair:
    def __init__(self, str, freq):
        self.str = str
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.str < other.str

        return self.freq > other.freq

def k_most_frequent_strings_max_heap(strs, k):
    hashmap = Counter(strs)

    max_heap = [Pair(str, freq) for str, freq in hashmap.items()]

    heapq.heapify(max_heap)

    return [heapq.heappop(max_heap).str for i in range(k)]

#Time complexity: O(n), O(m), O(m), O(klog(m)) => O(n+klog(n))
strs = ['go', 'coding','byte',
        'byte', 'go', 'interview',
        'interview', 'go'
        ]
k = 2
print(k_most_frequent_strings_max_heap(strs, k))

# import heapq
#
# # Sample data: item and frequency
# data = [('apple', 3), ('banana', 2), ('orange', 3), ('grape', 1)]
#
# # Creating the heap
# heap = []
# for item, freq in data:
#     # Push a tuple with negative frequency and the item
#     heapq.heappush(heap, (-freq, item))
#
# # Extract elements from the heap
# while heap:
#     freq, item = heapq.heappop(heap)
#     print(f"Item: {item}, Frequency: {-freq}")

