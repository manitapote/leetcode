#22 Generate parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, t):
            if l > n or r > n or l < r:
                return
            if l == n and r == n:
                ans.append(t)
                return
            dfs(l + 1, r, t + '(')
            dfs(l, r + 1, t + ')')

        ans = []
        dfs(0, 0, '')
        return ans




n = 3
print(Solution().generateParenthesis(n))
