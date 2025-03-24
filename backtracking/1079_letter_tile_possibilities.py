#1079 Letter Tile Possibilities

#Subset is different than subsequence
from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(cnt: Counter) -> int:
            ans = 0
            for i, x in cnt.items():
                if x > 0:
                    ans += 1
                    cnt[i] -= 1
                    ans += dfs(cnt)
                    cnt[i] += 1
            return ans

        cnt = Counter(tiles)
        return dfs(cnt)

tiles = 'ABC'
print(Solution().numTilePossibilities(tiles))


# x = {
#     'b': 2,
#     'c': 3
# }
#
# for i, j in x.items():
#     print('Before :', i, j)
#     x[i] = x[i] - 5
#     print('Sub :', x)
#     print('After :', i, j)
#     x[i] = x[i] + 9
#     print('Add :', x)


