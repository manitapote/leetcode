#921 Minimum add to make parantheses valid


class Solution:
    def minAddToMakeValid(self,
                          s: str
                          ) -> int:
        stack_open = []
        stack_close = []
        for x in s:
            if x == '(' and stack_close:
                stack_close.pop()
            elif x == ')' and stack_open:
                stack_open.pop()
            elif x == '(':
                stack_open.append(x)
            elif x == ')':
                stack_close.append(x)

        return max(len(stack_close), len(stack_open))





s="())"
a = Solution()
print(a.minAddToMakeValid(s))

s = "()))(("
print(a.minAddToMakeValid(s))
