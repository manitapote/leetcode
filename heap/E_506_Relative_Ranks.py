from typing import List
class Solution:
    def findRelativeRanks(self,
                          score: List[int]
                          ) -> List[str]:
        hash = {x: i for i, x in enumerate(score)}

        score.sort(reverse=True)

        result = [0]*len(score)
        for i, x in enumerate(score):
            if i == 0:
                result[hash[x]] = 'Gold Medal'
            elif i == 1:
                result[hash[x]] = 'Silver Medal'
            elif i == 2:
                result[hash[x]] = 'Bronze Medal'
            else:
                result[hash[x]] = f'{i+1}'
        return result






score = [5, 4, 3, 2, 1]
print(Solution().findRelativeRanks(score))
score = [10,3,8,9,4]
print(Solution().findRelativeRanks(score))
