from solver import has_one_solution
import numpy as np
import random

def count_zeros(grid):
    print(sum(1 for row in grid for col in row if col == 0))

def remove_numbers(grid, empty_spaces):
    indexes = [(row, col) for row in range(9) for col in range(9)]

    removals = 0
    while removals != empty_spaces:
        row, col = indexes.pop(random.randint(0, len(indexes)-1))
        number = grid[row][col]
        grid[row][col] = 0
        if removals >= 17:
            if has_one_solution(grid) is False:
                indexes.append((row, col))
                grid[row][col] = number
                continue
        removals += 1

    return grid


def random_solved_board():
    def pattern(row, col):
        return (3 * (row % 3) + row // 3 + col) % 9

    def shuffle(s):
        return random.sample(s, len(s))

    square = range(3)
    rows = [block * 3 + row for block in shuffle(square) for row in shuffle(square)]
    cols = [block * 3 + col for block in shuffle(square) for col in shuffle(square)]
    numbers = shuffle([n for n in range(1, 10)])

    board = [[numbers[pattern(row, col)] for col in cols] for row in rows]

    return board


def generate_board(difficulty):
    diff_nums = {
    'e': 36,
    'm': 34,
    'h': 30,
    'i': 27
    }

    empty_spaces = 81 - diff_nums[difficulty]
    grid = random_solved_board()
    grid = remove_numbers(grid, empty_spaces)

    return grid


grid = generate_board('i')
print(np.array(grid))
count_zeros(grid)