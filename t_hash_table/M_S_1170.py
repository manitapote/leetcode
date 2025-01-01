
#Words can repeat
from typing import List
import bisect

class Solution:
    def numSmallerByFrequency(self, 
                              queries: List[str], 
                              words: List[str]
                              ) -> List[int]:
       
        f = lambda s: s.count(min(s))
        fw = sorted(map(f, words))

        return [len(words) - bisect.bisect_right(fw, f(q)) for q in queries]


queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
obj = Solution()
print(obj.numSmallerByFrequency(queries,
                                words
                                ))
#Understanding logic
#find count of min character
#sort for search if to check how many above and
#how many below
#bisect_right gives index to be placed next which is same as
#staring from index 1