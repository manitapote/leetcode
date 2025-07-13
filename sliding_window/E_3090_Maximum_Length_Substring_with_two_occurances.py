from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self,
                               s: str
                               ) -> int:
        hashmap = defaultdict(int)
        max_length = 0
        l = 0
        for r, c in enumerate(s):
            hashmap[c] += 1

            while hashmap[c] > 2:
                hashmap[s[l]] -= 1
                l = l + 1

            max_length = max(max_length, r - l+1)

        return max_length


s = "bcbbbcba"
print(Solution().maximumLengthSubstring(s))
s = "aaaa"
print(Solution().maximumLengthSubstring(s))
s = "aadaad"
print(Solution().maximumLengthSubstring(s))