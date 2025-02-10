# 1768 Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.


class Solution:
    def mergeAlternately(self, word1, word2):
        #find the min length
        #loop and add strings
        #concat the remaining strings from longer string

        len_1 = len(word1)
        len_2 = len(word2)

        result = ''
        for i in range(max(len_1, len_2)):
            if i < len_1:
                result = result + word1[i]
            if i < len_2:
                result = result + word2[i]

        return result



word1 = "abc"
word2 = "pqr"
a = Solution()
print(a.mergeAlternately(word1, word2))
word1 = "ab"
word2 = "pqrs"
a = Solution()
print(a.mergeAlternately(word1, word2))
word1 = ""
word2 = "pqrs"
a = Solution()
print(a.mergeAlternately(word1, word2))
