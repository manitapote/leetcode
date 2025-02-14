# #205 Isomorphic Strings
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

#s, t, string
#s can replace t
#must preserve the order of the character
#no two character may overlap, but character may map to itself

class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        #many to one mapping not allowed
        map_s = {}
        map_t = {}
        # s = 'paper'
        # t = 'title'
        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = t[i]
            elif map_s[s[i]] != t[i]:
                return False

            if t[i] not in map_t:
                map_t[t[i]] = s[i]
            elif map_t[t[i]] != s[i]:
                return False


        return True





#one to one relation
#one to many relation
#many to one relation

#the qns is trying to say that one to many is not allowed?
#directional relation a -> b not equal to b -> a

s = 'egg'
t = 'add'
print(Solution().isIsomorphic(s, t))
s = 'foo'
t = 'bar'
print(Solution().isIsomorphic(s, t))
s = 'paper'
t = 'title'
print(Solution().isIsomorphic(s, t))
s = 'paperp'
t = 'tkyyz'
print(Solution().isIsomorphic(s, t))
s = "badc"
t = "baba"
print(Solution().isIsomorphic(s, t))
