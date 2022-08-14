from tkinter import *
from sudoku import sudoku_solution

root = Tk()
root.title("Sudoku Solver")

#displayed at the very beginning of the game
initial_label = Label(root, text = "Enter numbers you already know and click on solve")
initial_label.grid(row= 1, column= 1, columnspan= 10, pady= 5)

#displayed if the puzzle has no possible solution
error_label = Label(root, text= "", fg = "red")
error_label.grid(row= 2, column= 1, columnspan= 10, pady= 10)

#displayed if the puzzle is solvable and solved
solved_label = Label(root, text= "", fg = "green")
solved_label.grid(row= 2, column= 1, columnspan= 10, pady= 10)

cells = {}

# to check if the input is a valid number between 1-9
def validate_number(dgt):
    check = (dgt.isdigit() or dgt == "") and len(dgt) < 2
    return check

reg = root.register(validate_number)

# drawing a 3 x 3 grid and storing the data entered by the user in the grid cells
def draw_smaller_grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width= 7 , bg = bgcolor, justify= 'center', validate= 'key', validatecommand = (reg, "%dgt"))
            e.grid(row = row + i+1, column = column +j+1, sticky = "nsew", padx= 2, pady= 2, ipady = 14)
            cells[(row + i+1, column + j+1)] = e 

# drawing a 9 x 9 grid with alternate colours for the smaller grids
def draw_larger_grid():
    color = "#F7ECDE"
    for row in range(1, 10, 3):
        for column in range(0, 9, 3):
            draw_smaller_grid(row, column, color)
            if color == "#F7ECDE":
                color = "#9ED2C6"
            else:
                color = "#F7ECDE"

# to clear the entire grid after the puzzle has been solved
def clear_values():
    error_label.configure(text="")
    solved_label.configure(text="")
    for row in range(2,11):
        for col in range(1, 10):
            cells = cells[(row, col)]
            cells.delete(0, "end")

# to store all the values enter in the grid as a list in order to solve the puzzle
# 0 is added if no value is entered for the grid
def get_values():
    board = []
    error_label.configure(text="")
    solved_label.configure(text="")   
    for row in range(2,11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    update_grid(board)

# creating a button to solve the sudoku
btn = Button(root, command = get_values, text = "Solve Sudoku", width = 10)
btn.grid(row= 20, column= 2, columnspan= 5, pady= 10)

# creating a button to clear the grid
btn = Button(root, command = clear_values, text = "Clear Grid", width = 10)
btn.grid(row= 20, column= 4, columnspan= 5, pady= 10)

# updating the values in the displayed grid if a solution is present
def update_grid(grid):
    solution = sudoku_solution(grid)
    if solution != "Not Solvable":
        for row in range(2, 11):
            for column in range(1, 10):
                cells[(row, column)].delete(0, "end")
                cells[(row, column)].insert(0, solution[row - 2, column - 1])
        solved_label.configure(text= "Sudoku Solved")
    else:
        error_label.configure(text = "Sudoku not solvable")

draw_larger_grid()
root.mainloop()