import GUI
import time

def __main__():
    window = GUI.Window(1366, 768)

    puzzle = GUI.SudokuGrid(window, 100, 100)

    while True:
        puzzle.draw()
        window.tk.update()
        time.sleep(0.001)

if __name__ == "__main__":
    __main__()