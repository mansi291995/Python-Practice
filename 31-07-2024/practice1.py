
# alexWeight1=int(input("enter alexWeight1"))
# alexHeight1=float(input("enter alexHeight1"))
# brianWeight1=int(input("enter brianWeight1"))
# brianHeight1=float(input("enter brianHeight1"))
# alexBMI1 = alexWeight1 / (alexHeight1 ** 2)
# brianBMI1 = brianWeight1 / (brianHeight1 ** 2)
# alexHigherBMI1 = alexBMI1 > brianBMI1
# if alexHigherBMI1==True:
#     print("alex bmi is greater")
#     print("Alex's BMI:", alexBMI1)
#     print("Brian's BMI:", brianBMI1)
#     print("Is Alex's BMI higher than Brian's?", alexHigherBMI1)

# else:
#     print("brian bmi is greater")
#     print("Alex's BMI:", alexBMI1)
#     print("Brian's BMI:", brianBMI1)
#     print("Is Brian's BMI higher than Alex's?")

import tkinter as tk
import random

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048")
        self.grid_size = 4
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.main_grid = tk.Frame(self.master, bg="#92877d", bd=3, width=600, height=600)
        self.main_grid.grid(pady=(100, 0))
        self.cells = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                cell_frame = tk.Frame(self.main_grid, bg="#9e948a", width=150, height=150)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg="#9e948a")
                cell_number.grid(row=i, column=j)
                row.append(cell_number)
            self.cells.append(row)

    def start_game(self):
        self.matrix = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.spawn_new()
        self.spawn_new()
        self.update_gui()

    def spawn_new(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.matrix[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.matrix[i][j] = random.choice([2, 4])

    def update_gui(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j].configure(text="", bg="#9e948a")
                else:
                    self.cells[i][j].configure(text=str(cell_value), bg="#ede0c8")
        self.master.update_idletasks()

    def move(self, direction):
        if direction == 'up':
            self.matrix = self.transpose(self.matrix)
            self.matrix, moved = self.slide_and_merge(self.matrix)
            self.matrix = self.transpose(self.matrix)
        elif direction == 'down':
            self.matrix = self.transpose(self.matrix)
            self.matrix, moved = self.slide_and_merge(self.matrix, reverse=True)
            self.matrix = self.transpose(self.matrix)
        elif direction == 'left':
            self.matrix, moved = self.slide_and_merge(self.matrix)
        elif direction == 'right':
            self.matrix, moved = self.slide_and_merge(self.matrix, reverse=True)
        
        if moved:
            self.spawn_new()
            self.update_gui()

    def slide_and_merge(self, matrix, reverse=False):
        new_matrix = []
        moved = False
        for row in matrix:
            if reverse:
                row = row[::-1]
            new_row = [i for i in row if i != 0]
            merged_row = []
            skip = False
            for i in range(len(new_row)):
                if skip:
                    skip = False
                    continue
                if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
                    merged_row.append(new_row[i] * 2)
                    skip = True
                    moved = True
                else:
                    merged_row.append(new_row[i])
            merged_row += [0] * (self.grid_size - len(merged_row))
            if reverse:
                merged_row = merged_row[::-1]
            new_matrix.append(merged_row)
            if new_row != row:
                moved = True
        return new_matrix, moved

    def transpose(self, matrix):
        return [list(row) for row in zip(*matrix)]

def main():
    root = tk.Tk()
    game = Game2048(root)
    root.bind("<Up>", lambda event: game.move('up'))
    root.bind("<Down>", lambda event: game.move('down'))
    root.bind("<Left>", lambda event: game.move('left'))
    root.bind("<Right>", lambda event: game.move('right'))
    root.mainloop()

if __name__ == "__main__":
    main()
