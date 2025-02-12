# #118 Pascal's Triangle
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows):
        result = []
        for row in range(numRows):
            temp = [1]*(row+1)

            for j in range(1, len(temp) - 1):
                temp[j] = result[row - 1][j-1] + result[row - 1][j]


            result.append(temp)

        return result

numRows = 5
print(Solution().generate(numRows))

numRows = 1
print(Solution().generate(numRows))

numRows = 2
print(Solution().generate(numRows))


# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]