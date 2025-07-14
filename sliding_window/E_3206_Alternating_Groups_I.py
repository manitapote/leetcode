from typing import List
from collections import defaultdict
class Solution:
    def numberOfAlternatingGroups(self,
                                  colors: List[int]
                                  ) -> int:
        colors.append(colors[0])
        colors.append(colors[1])

        l = 0
        count = 0
        for r, color in enumerate(colors): #O(n)
            if r - l + 1 == 3:
                if colors[l:r+1] == [0,1,0] or colors[l:r+1] == [1, 0, 1]:
                    count += 1
                l += 1

        return count




#
colors = [1, 1, 1]
print(Solution().numberOfAlternatingGroups(colors))
colors = [0,1,0,0,1]
print(Solution().numberOfAlternatingGroups(colors))