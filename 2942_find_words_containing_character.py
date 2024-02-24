class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        # result = []
        # for i, word in enumerate(words):
        #     if x in word:
        #         result.append(i)

        return [i for i, word in enumerate(words) if x in word]


#29 ms

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        result = []
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
        return result

#38ms

a = Solution()
x = ['leet', 'code']
f = 'e'
j = a.findWordsContaining(x, f)
print(j)