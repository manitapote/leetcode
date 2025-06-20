#2375 Construct Smallest Number From DI String


class Solution:
    def smallestNumber(self,
                       pattern: str
                       ) -> str:
        result = []
        stack = []

        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            print('stack :', stack)
            print('result: ', result)
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())

        return ''.join(result)





pattern = "DIID"
a = Solution()
print(a.smallestNumber(pattern))

# pattern = "DDD"
# print(a.smallestNumber(pattern))
