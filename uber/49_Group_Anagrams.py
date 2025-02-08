# # 49 Group Anagrams
#
# Given an array of strings strs, group the
# anagrams
#  together. You can return the answer in any order.
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        key_hash = defaultdict(list)
        for x in strs:
            count = [0]*26
            for c in x:
                count[ord(c) - ord('a')] += 1

            key_hash[tuple(count)].append(x)

        return key_hash.values()


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = {}
#         for s in strs:
#             l = [0] * 26
#             for i in s:
#                 l[ord(i) - 97] += 1
#             t = tuple(l)
#             if t in d:
#                 d[t].append(s)
#             else:
#                 d[t] = [s]
#
#         ans = []
#         for an in d.values():
#             ans.append(an)
#
#         return ans





strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
a = Solution()
print(a.groupAnagrams(strs))
strs = [""]
a = Solution()
print(a.groupAnagrams(strs))
strs = ["a"]
a = Solution()
print(a.groupAnagrams(strs))


strs = ["eat", "tea",
        "tan", "ate",
        "nat", "bat"
        ]
a = Solution()
print(a.groupAnagrams(strs))
