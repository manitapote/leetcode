# 1823. Find the Winner of the Circular Game
from collections import deque
class Solution:
    def findTheWinner(self,
                      n: int,
                      k: int
                      ) -> int:
        people = list(range(1, n+1))
        positionToRemove = 0
        while len(people) > 1:
            positionToRemove = (positionToRemove + k - 1) % len(people)
            print(positionToRemove)
            people.pop(positionToRemove)
            # positionToRemove += 1

        return people[0]

#This is called Josephus formula
#T=O(n^2), S=O(n)



n=5
k=2
print(Solution().findTheWinner(n,k))


