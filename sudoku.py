# https://www.askpython.com/python/examples/sudoku-solver-in-python

N = 9

# solved puzzle output
def puzzle(a):
    for i in range(0, 9):
        for j in range(0, 9):
            return a[i][j]


# solving
def solve(grid, row, col, num):
    for i in range(9):
        # remove row duplicates
        if grid[row][i] == num:
            return False

    for j in range(9):
        # remove column duplicates
        if grid[j][col] == num:
            return False

    # check for the 3x3 grid
    row_start = row - row % 3
    col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + row_start][j + col_start] == num:  # check whether the 3x3 contain num
                return False
    return True


def sudoku(grid, row, col):
    if row == N - 1 and col == N:  # finish solving sudoku
        return True
    if col == N:
        row += 1  # start checking another row
        col = 0  # start checking from first column
    if grid[row][col] > 0:  # check whether the specific small cell is empty
        return sudoku(grid, row, col + 1)  # call function recursively
    for num in range(1, N + 1, 1):  # number 1 to 9 to be assigned
        if solve(grid, row, col, num):  # call function solve
            grid[row][col] = num  # assign num to the specific row and column if no replicate after checking
            if sudoku(grid, row, col + 1):  # check another column
                return True
        grid[row][col] = 0
    return False

