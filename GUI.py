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

    def __init__(self, window: Window):
        self.grid = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0], [
                5, 2, 0, 0, 0, 0, 0, 0, 0], [
                0, 8, 7, 0, 0, 0, 0, 3, 1], [
                    0, 0, 3, 0, 1, 0, 0, 8, 0], [
                        9, 0, 0, 8, 6, 3, 0, 0, 5], [
                            0, 5, 0, 0, 9, 6, 0, 0], [
                                1, 3, 0, 0, 0, 0, 2, 5, 0], [
                                    0, 0, 0, 0, 0, 0, 0, 7, 4], [
                                        0, 0, 5, 2, 0, 6, 3, 0, 0]]
        self.window = window

    def draw(self):
        x = 100
        y = 100
        for i in range(len(self.grid)):  # Rows
            for j in range(len(self.grid[i])):  # Columns
                self.window.canvas.create_line((x+1)*i, (y+1)*j, 500, 500)

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