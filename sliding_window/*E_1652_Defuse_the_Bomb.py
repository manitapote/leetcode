from typing import List
from itertools import accumulate

class Solution:
    def decrypt(self,
                code: List[int],
                k: int
                ) -> List[int]:

        ans = [0]*len(code)
        n = len(code)
        if k == 0:
            return ans

        s = list(accumulate(code+code, initial=0))
        print(code)
        print(s)
        for i in range(n):
            if k > 1:
                ans[i] = s[i+k+1] - s[i+1]
            else:
                ans[i] = s[i + n] - s[i + k + n]

            print(ans)

        return ans

# code = [5, 7, 1, 4]
# k = 3
# print(Solution().decrypt(code, k))
# code = [1,2,3,4]
# k = 0
# print(Solution().decrypt(code, k))
code = [2,4,9,3]
k = -2
print(Solution().decrypt(code, k))
