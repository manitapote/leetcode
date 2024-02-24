
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        total = 0
        for x in operations:
            if x in ['X++', '++X']:
                total += 1
            else:
                total -= 1

        return total

#Run time 60.03%

#Time : O(n)
#Space : O(1)

operations = ["++X","++X","X++"]
a = Solution()
total = a.finalValueAfterOperations(operations)
print(total)


class Solution:

    def add(self, x):
        return x + 1

    def sub(self, x):
        return x - 1

    def finalValueAfterOperations(self, operations):
        x = 0
        d = {
            '++X': self.add,
            'X++': self.add,
            'X--': self.sub,
            '--X': self.sub
        }
        for op in operations:
            x = d[op](x)
        return x

# Time complexity: O(n)
# Spacd complexity: O(1)
