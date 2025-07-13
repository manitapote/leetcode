class Solution:
    def minimumRecolors(self,
                        blocks: str,
                        k: int
                        ) -> int:

        countW = blocks[:k].count('W')
        min_flip = countW

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                countW += 1
            if blocks[i-k] == 'W':
                countW -= 1

            min_flip = min(min_flip, countW)

        return min_flip
                



blocks = "WBBWWBBWBW"
k = 7
print(Solution().minimumRecolors(blocks, k))
blocks = "WBWBBBW"
k = 2
print(Solution().minimumRecolors(blocks, k))