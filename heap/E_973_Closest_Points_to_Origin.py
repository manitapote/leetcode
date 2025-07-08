from typing import List
import math
import heapq
class Solution:
    def kClosest(self,
                 points: List[List[int]],
                 k: int
                 ) -> List[List[int]]:

        distance = [(math.sqrt((x)**2 + (y)**2), (x, y)) for x, y in points]
        heapq.heapify(distance)
        result = []
        for i in range(k):
            (dis, (x,y)) = heapq.heappop(distance)
            result.append([x, y])

        return result


points = [[1,3],[-2,2]]
k = 1
print(Solution().kClosest(points, k))
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(Solution().kClosest(points, k))
