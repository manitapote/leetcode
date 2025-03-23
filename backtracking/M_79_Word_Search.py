# from queue import deque
def word_search(matrix, word):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == word[0]:
                if dfs(row, column, matrix, word, 0):
                    return True

    return False

def dfs(row, column, matrix, word, index):
    if index == len(word):
        return True

    if not (0 <= row < len(matrix) and 0 <= column < len(matrix[0])):
        return False

    if matrix[row][column] != word[index]:
        return False

    temp = matrix[row][column]
    matrix[row][column] = None  # Mark as visited

    # Explore all four directions
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in dirs:
        new_row, new_column = row + dx, column + dy
        if dfs(new_row, new_column, matrix, word, index + 1):
            return True  # Return immediately if a correct path is found

    matrix[row][column] = temp  # Unmark as visited
    return False  # Return false after all directions have been explored



board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(word_search(board, word))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(word_search(board, word))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(word_search(board, word))