import unittest

from puzzle_reader import PuzzleReader


class TestPuzzleReader(unittest.TestCase):
    def test_read_json_file(self):
        # arrange
        file_path = "/home/hannah/Documents/FunProjects/Challenges/nonogram/test_nonogram.json"
        reader = PuzzleReader(file_path)

        # act
        puzzle = reader._read_json_puzzle_file()

        # assert
        assert len(puzzle) == 2

    def test_get_row_and_column_numbers(self):
        # arrange
        file_path = "/home/hannah/Documents/FunProjects/Challenges/nonogram/test_nonogram.json"
        reader = PuzzleReader(file_path)

        # act
        rows, columns = reader.get_row_and_column_numbers()

        # assert
        assert len(rows) == 10
        assert len(columns) == 10
