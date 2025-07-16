class Solution:
    def isSubsequence(self,
                      s: str,
                      t: str
                      ) -> bool:
        if len(s) > len(t):
            return False
        if s == '':
            return True

        i = 0
        for j in range(len(t)):
            if i > len(s) - 1:
                return False

            if s[i] == t[j]:
                if i == len(s) - 1:
                    return True

                i += 1

        return False


s = 'abc'
t = "ahbgdc"
print(Solution().isSubsequence(s, t))
s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))