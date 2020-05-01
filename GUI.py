from tkinter import *


class Window:

    def __init__(self, width: int, height: int):
        self.tk = Tk()
        self.tk.title = "Sudoku Solving Algorithm"
        self.canvas = Canvas(self.tk, width=width, height=height)
        self.canvas.pack()

    def close(self):
        self.tk.destroy()


class SudokuGrid:

    def __init__(self, window: Window, xPos: int, yPos: int):
        self.grid = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

        self.window = window
        self.cell_width = 50
        self.cell_height = 50
        self.xPos = 100
        self.yPos = 100

    def draw(self):
        for j in range(0, 9):  # Rows
            for i in range(0,9):  # Columns
                # Grid Lines
                self.window.canvas.create_rectangle(
                    self.xPos + i * self.cell_width,
                    self.yPos + j * self.cell_height,
                    self.xPos + i * self.cell_width + self.cell_width,
                    self.yPos + j * self.cell_height + self.cell_height)

                # Sudoku Numbers
                if self.grid[j][i] != 0:
                    num = Label(
                        text=self.grid[j][i], font=(
                            "Helvetica", 16), justify=CENTER)
                    num.place(x=(self.xPos + i * self.cell_width+10),
                            y=(self.yPos + j * self.cell_height+10))

    def is_valid(self) -> bool:
        for row in self.grid:
            for column in row:
                if self.grid[row][column] < 0 or self.grid[row][column] > 9:
                    return False

        for row in self.grid:
            if sum(row) > 45:
                return False

        for i in range(0, len(self.grid)):
            column_sum = 0
            for j in range(0, len(i)):
                column_sum += self.grid[i][j]
            if column_sum > 45:
                return False
