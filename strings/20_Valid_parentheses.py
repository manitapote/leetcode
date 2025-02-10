#20 Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

from collections import deque
class Solution:
    def isValid(self, s):
        check = []
        check_x = None
        for x in s:
            if x in ['(', '{', '[']:
                check.append(x)
                continue
            elif x in [')', '}', ']']:
                if not check:
                    return False

                check_x = check.pop()

                if x == ')' and check_x != '(':
                    return False
                if x == '}' and check_x != '{':
                    return False

                if x == ']' and check_x != '[':
                    return False


        return len(check) == 0





s = '()'
a = Solution()
print(a.isValid(s))

s = "()[]{}"
a = Solution()
print(a.isValid(s))

s = "(]"
a = Solution()
print(a.isValid(s))
s = "([])"
a = Solution()
print(a.isValid(s))