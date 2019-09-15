from puzzle_reader import PuzzleReader


class PuzzleSolver:

    def __init__(self):
        self.row_nums = None
        self.column_nums = None
        self.size = None

    def solve_puzzle_from_file(self, file_path):
        reader = PuzzleReader(file_path)
        self.row_nums, self.column_nums = reader.get_row_and_column_numbers()
        self.size = len(self.row_nums)

    def is_full_line(self, line_nums):
        if sum(line_nums) + len(line_nums) - 1 == self.size:
            return True
        return False
