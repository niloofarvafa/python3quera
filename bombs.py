
n, m = map(int, input().split())
k = int(input())
grid = [[0] * m for _ in range(n)]

# Read bomb positions and mark grid
for _ in range(k):
    row, col = map(int, input().split())
    row -= 1  # Convert to zero-based index
    col -= 1
    grid[row][col] = '*'  # Mark the bomb location

    # Update adjacent cells
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < n and 0 <= j < m and grid[i][j] != '*':
                grid[i][j] += 1

# Output the grid
for row in grid:
    print(' '.join(map(str, row)))
Python