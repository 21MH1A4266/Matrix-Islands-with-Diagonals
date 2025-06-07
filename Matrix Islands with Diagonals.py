# Matrix Islands with Diagonals

def is_safe(matrix, visited, row, col):
    return (0 <= row < len(matrix)) and (0 <= col < len(matrix[0])) and (matrix[row][col] == 1 and not visited[row][col])

def dfs(matrix, visited, row, col):
    row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    visited[row][col] = True
    
    for k in range(8):
        if is_safe(matrix, visited, row + row_nbr[k], col + col_nbr[k]):
            dfs(matrix, visited, row + row_nbr[k], col + col_nbr[k])

def count_islands(matrix):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    count = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(matrix, visited, i, j)
                count += 1
                
    return count

# Example usage
matrix = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0]
]

print("Number of islands:", count_islands(matrix))
