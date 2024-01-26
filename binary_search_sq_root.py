class Solution():
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        end = x
        start = 0
        res = 0
        while start <= end:
            print(start, end)
            mid = (start + end) //2
            sq = mid * mid
            if sq < x:
                start = mid + 1
                res = mid
            elif sq > x:
                end = mid - 1
            elif sq == x:
                res = mid
                return res
        return res




x = 2
a = Solution().mySqrt(x)
print(a)
