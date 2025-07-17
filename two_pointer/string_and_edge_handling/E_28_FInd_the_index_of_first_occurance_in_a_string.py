class Solution:
    def strStr(self,
               haystack: str,
               needle: str
               ) -> int:
        r = 0
        l = 0
        while r < len(haystack):
            if needle == haystack[r:r+len(needle)]:
                return r

            r += 1
        return -1


haystack = "sadbutsad"
needle = "sad"
print(Solution().strStr(haystack, needle))
haystack = "leetcode"
needle = "leeto"
print(Solution().strStr(haystack, needle))