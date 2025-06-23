# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
#
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


from typing import List, Optional
class Solution:
    def findJudge(self,
                  n: int,
                  trust: List[List[int]]
                  ) -> int:
        nodes_a = [0] * (n+1)
        for i, j in trust:
            nodes_a[i] -= 1
            nodes_a[j] += 1

        for i in range(1, n+1):
            if nodes_a[i] == (n-1):
                return i

        return -1




n = 2
trust = [[1, 2]]
a = Solution()
print(a.findJudge(n, trust))

n=3
trust = [[1,2],[2,3]]
print(a.findJudge(n, trust))

n = 3
trust = [[1,3],[2,3],[3,1]]
print(a.findJudge(n, trust))

n = 3
trust = [[1,3],[2,3]]
print(a.findJudge(n, trust))
