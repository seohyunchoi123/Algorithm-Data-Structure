# Question Link: https://www.hackerrank.com/challenges/bomber-man/problem

def next_situation(grid):
    row = len(grid)
    col = len(grid[0])
    new_grid = [[-1]*col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 'O':
                new_grid[i][j] = '.'
                if i+1 < row:
                    new_grid[i+1][j] = '.'
                if i-1 > -1:
                    new_grid[i-1][j] = '.'
                if j+1 < col:
                    new_grid[i][j+1] = '.'
                if j-1 > -1:
                    new_grid[i][j-1] = '.'
            elif grid[i][j] == '.' and new_grid[i][j] == -1:
                new_grid[i][j] = 'O'
    return new_grid

def bomberMan(n, grid):
    row = len(grid)
    col = len(grid[0])
    if n == 1:
        ans = grid
    elif n % 2 == 0:
        ans = [['O']*col for _ in range(row)]
    elif n % 4 == 1:
        ans = next_situation(next_situation(grid))
    else:
        ans = next_situation(grid)
    for i in range(row):
        ans[i] = "".join(ans[i])
    return ans


# Time Complexity: O(r * c)
# Space Complexity: O(r * c)
# Restrict: 1 <= r, c <= 200
