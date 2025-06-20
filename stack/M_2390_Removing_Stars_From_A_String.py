#2390 Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for x in s:
            if x == '*':
                stack.pop()
            else:
                stack.append(x)

        return ''.join(stack)



s = "leet**cod*e"
a = Solution()
print(a.removeStars(s))

s = "erase*****"
print(a.removeStars(s))