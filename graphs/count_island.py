def count_island(matrix):
    #T=O(n^2)
    count = 0
    for i, x in enumerate(matrix):
        for j, y in enumerate(x):
            if matrix[i][j] == 1:
                dfs(i, j, matrix)
                count += 1

    return count

def dfs(i, j, matrix):
    matrix[i][j] = -1

    dirs = [(-1,0), (1,0), (0, -1), (0, 1)]
    for row, column in dirs:
        new_r = i + row
        new_c = j + column

        if check_bound(new_r, new_c, matrix) and matrix[new_r][new_c] == 1:
            dfs(new_r, new_c, matrix)

def check_bound(i, j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

#Time: considering if the rows and column are same
#T= O(n^2) else O(m.n)
#S=O(m.n) for recursive case





matrix = [[1,1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0 , 0, 1]]
print(count_island(matrix))
