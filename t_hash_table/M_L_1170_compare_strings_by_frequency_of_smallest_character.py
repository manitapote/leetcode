from typing import List

#Words can repeat
class Solution:
    def numSmallerByFrequency(self, 
                              queries: List[str], 
                              words: List[str]
                              ) -> List[int]:
        
        track = []
        keys = []
        for word in words:
            keys.append(word)
            track.append(self.find_frequency(word))

        result = []
        for x in queries:
            num = self.find_frequency(x)
            total = 0

            for val in track:
                if num < val:
                    total+=1

            result.append(total)
        
        return result

    def find_frequency(self, 
                       text: str
                       ):
        min_char = text[0]
        count = 1
        for i, x in enumerate(text):
            if i == 0:
                continue
            if ord(x) == ord(min_char):
                count += 1
            if ord(x) < ord(min_char):
                min_char = x
                count = 1
            

        return count

    
obj = Solution()
queries = ["cbd"]
words = ["zaaaz"]

queries = ["ba","a","baaa","aaabbbab","abbbb","bb",
           "aaaababbba","babaaababb","bbb","b",
           "aaaaa","babbbaab","bbbaaabab","bba",
           "baabbaaab","bbabbababa","aaabbab","aaab"]
words = ["bab","bab","bbaaaaab","aa","ab","bb","bbbaba",
         "bb","bba","aba","ba","babbbabaab","baaabb",
         "abaa","b","abbabbb","b","abbbba"]

result = obj.numSmallerByFrequency(
        queries,
        words
        )
print(result)