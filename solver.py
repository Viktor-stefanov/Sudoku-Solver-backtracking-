GREEN = (10, 250, 10)
RED = (250, 10, 10)


def is_valid(bo, num, row, col):
    # check row
    for i in range(9):
        if bo[i][col] == num and i != row:
            return False
    # check column
    for i in range(9):
        if bo[row][i] == num and i != col:
            return False

    # check square
    square_w = (row // 3) * 3
    square_h = (col // 3) * 3
    for sRow in range(square_w, square_w + 3):
        for sCol in range(square_h, square_h + 3):
            if bo[sRow][sCol] == num and (sRow, sCol) != (row, col):
                return False

    return True


def solutions(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, num, row, col):
                        grid[row][col] = num
                        yield from solutions(grid)
                        grid[row][col] = 0
                return
    yield grid


def has_one_solution(grid):
    sols = 0
    grid_copy = [row[:] for row in grid]
    for solution in solutions(grid_copy):
        sols += 1
        if sols > 1:
            return False
    return True if sols == 1 else False


def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, num, row, col):
                        grid[row][col] = num
                        solve(grid)
                        grid[row][col] = 0
                return