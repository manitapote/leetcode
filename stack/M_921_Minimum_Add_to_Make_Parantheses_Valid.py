#921 Minimum add to make parantheses valid


class Solution:
    def minAddToMakeValid(self,
                          s: str
                          ) -> int:
        stack = []
        for x in s:
            if x == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(x)

        return len(stack)





s="())"
a = Solution()
print(a.minAddToMakeValid(s))

s = "()))(("
print(a.minAddToMakeValid(s))
