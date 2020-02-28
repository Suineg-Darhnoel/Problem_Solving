# Using Backtracking algorithm to solve Sudoku
import numpy as np
grid1 =   [
            [0,0,0,0,0,8,7,0,5],
            [0,6,0,0,7,0,0,8,0],
            [0,7,0,0,0,3,2,0,9],
            [9,0,0,8,1,7,5,0,3],
            [5,0,0,3,0,6,0,0,7],
            [2,0,7,4,5,9,0,0,8],
            [7,0,8,2,0,0,0,5,0],
            [0,5,0,0,8,0,0,9,0],
            [1,0,3,6,0,0,0,0,0]
        ]
grid2 =   [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
          ]

# To print a clean grid
def smart_print(grid):
    print(np.array(grid))

# To varify if the value is in the
# same row, col or block
def varified(grid, row, col, val):
    def block_head(row, col):
        row_id = (row//3)%3
        col_id = (col//3)%3
        return (3*row_id, 3*col_id)

    # row checking
    if val in grid[row]:
        return False

    # column checking
    for r in grid:
        if val == r[col]:
            return False

    rhead, chead = block_head(row, col)
    block_arr = [
                grid[y][x]
                for y in range(rhead, rhead+3)
                for x in range(chead, chead+3)
            ]
    # print(block_arr)
    # box checking
    if val in block_arr:
        return False
    return True

# Find the first unassigned position
def unassigned(grid):
    for irow, row in enumerate(grid):
        for icol, col in enumerate(row):
            if col == 0:
                return (irow, icol)
    return None

# Solve the problem using recursion
def backtrack_solve(grid):
    if not unassigned(grid):
        return True
    row, col = unassigned(grid)
    for i in range(1, 10):
        if varified(grid, row, col, i):
            grid[row][col] = i

            if backtrack_solve(grid):
                return True

            grid[row][col] = 0
    return False


if __name__ == "__main__":
    smart_print(grid1)
    backtrack_solve(grid1)
    smart_print(grid1)

    smart_print(grid2)
    backtrack_solve(grid2)
    smart_print(grid2)

