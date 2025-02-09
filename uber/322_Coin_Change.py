# #322 Coin Change
#
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.

#Bottom up dynamic programming
class Solution:

    def coinChange(self, coins, amount):
        dp =[float('inf')]* (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    # 1 here is because c can be used
                    #once, need to find remaining
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] != float('inf') else -1



coins = [1,2,5]
amount = 11

a = Solution()
print(a.coinChange(coins, amount))


coins = [2]
amount = 3
a = Solution()
print(a.coinChange(coins, amount))

coins = [1]
amount = 0
a = Solution()
print(a.coinChange(coins, amount))
