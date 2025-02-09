# 70 Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#


class Solution:
    def climbStairs(self, n):
        one =1
        two = 1
        for x in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one




n = 2
a = Solution()
print(a.climbStairs(n))

n = 3
a = Solution()
print(a.climbStairs(n))

n = 4
a = Solution()
print(a.climbStairs(n))


