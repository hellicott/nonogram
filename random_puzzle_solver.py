from puzzle_reader import PuzzleReader
from grid import Grid
import random


class SlightlyBetterThanRandomNonogramSolver:

    def __init__(self, grid: Grid, reader: PuzzleReader):
        self.grid = grid
        self.row_nums, self.col_nums = reader.get_row_and_column_numbers()

    # def solve(self):
    #     for i in range(self.grid.size):


    def solve_row(self, original_string, row_nums):
        print("Original String: {}".format(original_string))
        row_string = original_string
        percentage = self.calculate_percentage(original_string, row_nums)
        num_of_tries = 0
        while not self.is_row_solved(row_string, row_nums):
            num_of_tries += 1
            row_string = self.fill_row_with_random_squares(percentage, original_string)
            print("Attempt Number {}: {}".format(num_of_tries, row_string))
        print("Solved: {} in {} attempts".format(row_string, num_of_tries))
        return row_string

    def fill_row_with_random_squares(self, percentage, row_sting):
        new_string = ""
        for square in row_sting:
            if square != "X" and square != "_":
                new_string += self.choose_value(random.randint(1, 100), percentage)
            else:
                new_string += square
        return new_string

    @staticmethod
    def choose_value(rand_int, percentage):
        if rand_int < percentage:
            return "X"
        else:
            return "_"

    def calculate_percentage(self, row_string, row_nums):
        num_of_undecided_squares = row_string.count(".")
        num_of_decided_squares = row_string.count("X")
        expected_num_of_decided_squares = sum(row_nums)
        num_squares_required_to_be_decided = expected_num_of_decided_squares - num_of_decided_squares
        percentage = num_squares_required_to_be_decided / num_of_undecided_squares
        return percentage * 100

    @staticmethod
    def _as_row_nums(row_string):
        split_list = row_string.replace(".", "").split("_")
        length_list = [len(x) for x in split_list]
        while 0 in length_list:
            length_list.remove(0)
        if len(length_list) == 0:
            return [0]
        else:
            return length_list

    def is_row_solved(self, row_string, row_nums):
        return self._as_row_nums(row_string) == row_nums

    def fill_definite_squares_in_row(self):
        for i in range(self.grid.size):
            if sum(self.row_nums[i]) > self.grid.size/2:
                row = self.find_definite_squares_in_line(self.row_nums[i])
                self.grid.insert_row_to_grid(row, i)

    def fill_definite_squares_in_column(self):
        for i in range(self.grid.size):
            if sum(self.col_nums[i]) > self.grid.size / 2:
                row = self.find_definite_squares_in_line(self.col_nums[i])
                self.grid.insert_column_to_grid(row, i)

    def find_definite_squares_in_line(self, line_numbers):
        line_string = ""
        forwards_line = self.get_numbers_as_line(line_numbers)
        backwards_line = forwards_line[::-1]
        for i in range(self.grid.size):
            total = forwards_line[i] + backwards_line[i]
            if total > 1:
                line_string += "X"
            else:
                line_string += "."
        return line_string

    def get_numbers_as_line(self, numbers):
        line_list = []
        for number in numbers:
            line_list.extend([1] * number)
            line_list.extend([0] * 1)
        # make line correct length
        if len(line_list) > self.grid.size:
            line_list = line_list[0:self.grid.size]
        elif len(line_list) < self.grid.size:
            diff = self.grid.size - len(line_list)
            line_list.extend([0] * diff)
        return line_list


def main():
    grid = Grid(5)
    path = r"/home/hannah/Documents/FunProjects/Challenges/nonogram/test_nonogram_5x5.json"
    reader = PuzzleReader(path)
    solver = SlightlyBetterThanRandomNonogramSolver(grid, reader)
    solver.solve_row("X....", solver.row_nums[1])


if __name__ == "__main__":
    main()
