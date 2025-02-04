# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        charSet = set()
        res = 0
        if len(s) == 1:
            return 1
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)

        return res



s = "abcabcbb"
a = Solution()
print(a.lengthOfLongestSubstring(s))

s = "bbbbb"
a = Solution()
print(a.lengthOfLongestSubstring(s))

s = "pwwkew"
a = Solution()
print(a.lengthOfLongestSubstring(s))

s = "au"
a = Solution()
print(a.lengthOfLongestSubstring(s))

s = "aab"
a = Solution()
print(a.lengthOfLongestSubstring(s))

