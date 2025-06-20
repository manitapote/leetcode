# 1047 Remove all adjacent duplicates in string
#
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
#
# We repeatedly make duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        new_str = ''
        for x in s:
            if stack and stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)

        return ''.join(stack)


s = "abbaca"
a = Solution()
print(a.removeDuplicates(s))
s = "azxxzy"
print(a.removeDuplicates(s))
