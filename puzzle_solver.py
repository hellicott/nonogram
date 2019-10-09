from puzzle_reader import PuzzleReader
from grid import Grid


class PuzzleSolver:

    def __init__(self, grid: Grid):
        self.grid = grid
        self.row_nums = None
        self.column_nums = None
        self.size = grid.size
        self.solved_rows = []

    def solve_puzzle_from_file(self, file_path):
        reader = PuzzleReader(file_path)
        self.row_nums, self.column_nums = reader.get_row_and_column_numbers()
        self.size = len(self.row_nums)

    def fill_definite_squares_in_grid(self):
        i = 0
        for row_num in self.row_nums:
            definite_row = self.find_definite_squares_in_line(row_num)
            self.grid.insert_row_to_grid(definite_row, i)
            i += 1
        i = 0
        for column_num in self.column_nums:
            definite_column = self.find_definite_squares_in_line(column_num)
            self.grid.insert_column_to_grid(definite_column, i)
            i += 1

    def find_definite_squares_in_line(self, line):
        line_list = []
        forwards_line = self.get_numbers_as_line(line)
        backwards_line = forwards_line[::-1]
        for i in range(self.size):
            sum = forwards_line[i] + backwards_line[i]
            if sum > 1:
                line_list.append("X")
            else:
                line_list.append(".")
        return line_list

    def get_numbers_as_line(self, numbers):
        line_list = []
        for number in numbers:
            line_list.extend([1] * number)
            line_list.extend([0] * 1)
        if len(line_list) > self.size:
            line_list = line_list[0:self.size]
        elif len(line_list) < self.size:
            diff = self.size - len(line_list)
            line_list.extend([0] * diff)
        return line_list

    def is_full_line(self, line_nums):
        if sum(line_nums) + len(line_nums) - 1 == self.size:
            return True
        return False

    def is_solved(self):
        return self.grid.calculate_line_numbers(row=True) == self.row_nums and \
               self.grid.calculate_line_numbers(row=False) == self.column_nums

    def is_solved_2(self):
        correct = "XX-XX\n" \
                  "XX-XX\n" \
                  "-----\n" \
                  "X---X\n" \
                  "-XXX-\n"
        print(correct)
        return str(self.grid) == correct
