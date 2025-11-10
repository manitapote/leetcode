from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    count += 1
                    self.dfs(row, column, grid)

        return count

    def dfs(self, row, column, grid):

        if 0 <= row < len(grid) and 0 <= column < len(grid[0]) and grid[row][column] == '1':
            grid[row][column] = '-1'
            self.dfs(row + 1, column, grid)
            self.dfs(row - 1, column, grid)
            self.dfs(row, column + 1, grid)
            self.dfs(row, column - 1, grid)

        return


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(Solution().numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))