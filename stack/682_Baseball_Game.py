# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
#
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
#
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
#
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
#

from typing import List, Optional
class Solution:
    def calPoints(self,
                  operations: List[str]
                  ) -> int:
        stack = []
        for x in operations:
            if x == 'C':
                stack.pop()
            elif x == 'D' :
                stack.append(2*stack[-1])
            elif x == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(x))

            print(stack)

        return sum(stack)


# ops = ["5","2","C","D","+"]
a = Solution()
# print(a.calPoints(ops))


ops = ["5","-2","4","C","D","9","+","+"]
print(a.calPoints(ops))

ops = ["1","C"]
print(a.calPoints(ops))