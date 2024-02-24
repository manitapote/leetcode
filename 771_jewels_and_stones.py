import re
class Solution(object):
    # 16ms
    # Time complexity = O(n)
    # Space complexity = O(1)
    def numJewelsInStones(self, jewels: str, stones: str):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        total = 0

        for s in stones:
            if s in jewels:
                total+= 1
        return total

    #28ms
    # def numJewelsInStones(self, jewels, stones):
    #     s = re.sub(f'[{jewels}]', '', stones)
    #     return len(stones) - len(s)


    #18ms
    def numJewelsInStones(self, J, S):
        return sum(map(S.count, J))



jewels = "aA"
stones = "aAAbbbb"

a = Solution()
print(a.numJewelsInStones(jewels, stones))