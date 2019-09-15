import random
import math

class Grid:

    def __init__(self, size):
        self.size = size
        self.row_strings = [""] * self.size
        self.column_strings = [""] * self.size
        self.grid = self.build_grid()

    def setup_puzzle(self, mode="random"):
        if mode == "random":
            self.generate_random_solution()
        else:
            # other method of creating puzzle
            pass
        self._rows_and_columns_to_strings()

    def build_grid(self):
        grid = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append('.')
            grid.append(row)
        return grid

    def generate_random_solution(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.rand_bool():
                    self.grid[row][column] = "0"

    def _rows_and_columns_to_strings(self):
        self.row_strings = [""] * self.size
        self.column_strings = [""] * self.size
        for row in range(self.size):
            for column in range(self.size):
                self.row_strings[row] += (self.grid[row][column])
                self.column_strings[column] += (self.grid[row][column])

    @staticmethod
    def calculate_group_lengths(row_or_column_string):
        split_list = row_or_column_string.split(".")
        length_list = [len(x) for x in split_list]
        while 0 in length_list: length_list.remove(0)
        if len(length_list) == 0:
            return [0]
        else:
            return length_list

    @staticmethod
    def rand_bool(percent=50):
        return random.randrange(100) < percent

    def __str__(self):
        grid_string = " _" * self.size
        grid_string += "\n"
        for row in self.grid:
            grid_string += "|"
            for thing in row:
                grid_string += thing
                grid_string += "|"
            grid_string += "\n"
        grid_string += " ¯" * self.size
        return grid_string
