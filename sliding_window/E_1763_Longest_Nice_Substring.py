class Solution:
    def longestNiceSubstring(self,
                             s: str
                             ) -> str:
        if len(s) < 2:
            return ''

        charset = set(s)
        for i, character in enumerate(s):
            if character.swapcase() not in charset:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                return left if len(left) >= len(right) else right

        return s

s = 'YazaAay'
print(Solution().longestNiceSubstring(s))
s = "Bb"
print(Solution().longestNiceSubstring(s))
s = 'c'
print(Solution().longestNiceSubstring(s))