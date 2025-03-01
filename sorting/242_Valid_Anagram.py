# # Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# Example
# 1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example
# 2:
#
# Input: s = "rat", t = "car"
#
# Output: false
from collections import Counter

class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

        # track_s = {}
        # track_y = {}
        # for i in range(len(s)):
        #     if s[i] in track_s:
        #         track_s[s[i]] += 1
        #     else:
        #         track_s[s[i]] = 1
        #
        #     if t[i] in track_y:
        #         track_y[t[i]] += 1
        #     else:
        #         track_y[t[i]] = 1
        #
        # return track_y == track_s

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))

s = "rat"
t = "car"
print(Solution().isAnagram(s, t))