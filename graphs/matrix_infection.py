#find the matrix infection
from queue import deque
def find_time_of_matrix_infection(matrix):
    count = 0
    count_1 = 0
    queue = deque([])
    for i, x in enumerate(matrix):
        for j, y in enumerate(x):
            if matrix[i][j] == 2:
                queue.append((i, j))
            if matrix[i][j] == 1:
                count_1 += 1

    return bfs(queue, matrix, count_1, count)


def bfs(queue, matrix, count_1, count):
    dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]
    while queue and count_1 > 0:
        #count_1 greater than 0 make sure we are not doing the changes when we
        #reach leaf node
        count += 1
        for i in range(len(queue)):
            row, column = queue.popleft()
            for i, j in dirs:
                new_row = row+i
                new_column = column+j

                if valid_cell(new_row, new_column, matrix) and matrix[new_row][new_column] == 1:
                    matrix[new_row][new_column] = 2
                    count_1 -= 1
                    queue.append((new_row, new_column))

    return count if count_1 == 0 else -1
def valid_cell(row, column, matrix):
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])

matrix = [[1,1,1,0], [0,0,2,1], [0,1,1,0]]
print(find_time_of_matrix_infection(matrix))
