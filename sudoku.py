import numpy as np

# SOLVES THE SUDOKU PUZZLE
def possible(grid, row, column, num):
    # Checks if the number is present across the row
    for i in range(9):
        if grid[i][row] == num and i != column: 
            return False

    # Checks if the number is present across the column
    for i in range(9):
        if grid[column][i] == num and i != row:
            return False

    # Checks if the number in the small 3 x 3 grid
    row_start = (row // 3) * 3
    column_start = (column // 3) * 3
    for X in range(row_start, row_start + 3):
        for Y in range(column_start, column_start + 3):  
            if grid[Y][X] == num:
                return False    
    return True

def solve_sudoku(grid, row, column):
    # if the recursor reaches the last cell and the entire grid is filled
    if row == 8 and column == 9:
        return True
    
    # moves to the next row once the current row is completely filled
    if column == 9:
        row += 1
        column = 0

    # if the value is already provided by the user then shift to the adjacent cell
    if grid[row][column] > 0:
        return solve_sudoku(grid, row, column + 1)

    # for any empty cell, it checks all the possible values that can fit the cell
    for num in range(1, 10):
        if possible(grid, row, column, num):
            grid[row][column] = num
            
            # if the number chosen is not the solution to the cell
            if solve_sudoku(grid, row, column + 1):
                return True

        # return the cell value to 0
        grid[row][column] = 0
    return False

# if the sudoku is solvable, then update the values
def sudoku_solution(grid):
    if solve_sudoku(grid, 0, 0):
        return grid
    else:
        return "Not solvable"