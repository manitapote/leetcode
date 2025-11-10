from typing import List
from queue import deque
class Solution:
    def numOfIsland(self, grid: List[List[str]]) -> int:
        count = 0
        found = deque([])
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    found.append((row, column))
                    count += self.bfs(found, grid)

        return count

    def bfs(self, found, grid):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while found:
            row, column = found.pop()
            grid[row][column] = "-1"

            for x, y in dirs:

                new_row = row + x
                new_column = column + y
                if self.valid(new_row, new_column, grid):
                    found.append((new_row, new_column))


        return 1



    def valid(self, new_row, new_column, grid):
        if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]) and grid[new_row][new_column] == '1':
            return True

        return False




grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(Solution().numOfIsland(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numOfIsland(grid))