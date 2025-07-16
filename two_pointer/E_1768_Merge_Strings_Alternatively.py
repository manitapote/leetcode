class Solution:
    def mergeAlternately(self,
                         word1,
                         word2
                         ):
        result = ''
        total1 = len(word1)
        total2 = len(word2)
        for i in range(min(total2, total1)):
            result += word1[i]
            result += word2[i]

        if total2 == total1:
            return result

        if total2 > total1:
            result += word2[i+1:]
        else:
            result += word1[i+1:]

        return result


word1 = "abc"
word2 = "pqr"
print(Solution().mergeAlternately(word1, word2))
word1 = "ab"
word2 = "pqrs"
print(Solution().mergeAlternately(word1, word2))