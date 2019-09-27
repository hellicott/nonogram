from puzzle_reader import PuzzleReader
from grid import Grid


class SlightlyBetterThanRandomNonogramSolver:

    def __init__(self, grid: Grid, reader: PuzzleReader):
        self.grid = grid
        self.row_nums, self.col_nums = reader.get_row_and_column_numbers()

    @staticmethod
    def as_row_nums(row_string):
        split_list = row_string.split("_")
        length_list = [len(x) for x in split_list]
        while 0 in length_list:
            length_list.remove(0)
        if len(length_list) == 0:
            return [0]
        else:
            return length_list

    def is_row_solved(self, row_string, row_nums):
        return self.as_row_nums(row_string) == row_nums