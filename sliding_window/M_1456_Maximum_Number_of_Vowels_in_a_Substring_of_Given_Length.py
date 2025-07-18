class Solution:
    def maxVowels(self,
                  s: str,
                  k: int
                  ) -> int:
        vowels = set('aeiou')
        ans = cnt = sum(c in vowels for c in s[:k])
        for i in range(k, len(s)):
            cnt += int(s[i] in vowels) - int(s[i-k] in vowels)
            ans = max(ans, cnt)
        return ans

#string is immutable

s = 'abciiidef'
k = 3
print(Solution().maxVowels(s, k))
s = "aeiou"
k = 2
print(Solution().maxVowels(s, k))
s = "leetcode"
k = 3
print(Solution().maxVowels(s, k))


