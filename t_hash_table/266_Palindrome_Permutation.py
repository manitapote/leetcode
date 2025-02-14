# #266 Palindrome Permutation
#
# Given a string s, return true if a permutation of the string could form a
# palindrome
#  and false otherwise.

class Solution:
    def canPermutePalindrome(self, s):
        count = {}
        for x in s:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        odd = 0
        for (key, value) in count.items():
            if value % 2 == 1:
                odd += 1
            if odd > 1:
                return False

        return True



s = 'code'
print(Solution().canPermutePalindrome(s))
s = 'aab'
print(Solution().canPermutePalindrome(s))
s = "carerac"
print(Solution().canPermutePalindrome(s))
s = "aabb"
print(Solution().canPermutePalindrome(s))
s = "aacccbb"
print(Solution().canPermutePalindrome(s))

