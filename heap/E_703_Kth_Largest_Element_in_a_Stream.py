from typing import List
import heapq
class KthLargest:

    def __init__(self,
                 k: int,
                 nums: List[int]
                 ):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) #O(n)
        #Space=O(n)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums) #O((n-k)log(n))
            #Space = O(k)

        #Total = O(n) + O((n-k)log(n)) = log(nlog(n))

    def add(self,
            val: int
            ) -> int:
        heapq.heappush(self.nums, val)
        #O(log(k)) k = size of heap
        #Space = O(k)

        while len(nums) > self.k:
            heapq.heappop(self.nums) #O(log(k)) #O(log(k))

        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:

k = 3
nums = [4,5,8,2]
obj = KthLargest(k, nums)
val = 3
param_1 = obj.add(val)
val = 5
param_1 = obj.add(val)
val = 10
param_1 = obj.add(val)
val = 9
param_1 = obj.add(val)
val = 4
param_1 = obj.add(val)

#Total time complexity: O(n+nlog(n))
#Space = O(n)