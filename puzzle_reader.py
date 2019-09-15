import json


class PuzzleReader:
    def __init__(self, path_to_json_puzzle_file):
        self.path = path_to_json_puzzle_file

    def _read_json_puzzle_file(self):
        with open(self.path) as puzzle_file:
            puzzle = json.load(puzzle_file)
            return puzzle

    def get_row_and_column_numbers(self):
        puzzle = self._read_json_puzzle_file()
        row_numbers = puzzle["rows"]
        column_numbers = puzzle["columns"]
        return row_numbers, column_numbers
