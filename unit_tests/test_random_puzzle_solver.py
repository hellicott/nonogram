from unittest import TestCase, mock

from random_puzzle_solver import SlightlyBetterThanRandomNonogramSolver as Solver
from puzzle_reader import PuzzleReader
from grid import Grid


class TestRandomPuzzleSolver(TestCase):

    def test_as_row_nums_returns_correct_array_for_single_group(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        row_string = "_XX__"

        # act
        row_nums = solver.as_row_nums(row_string)

        # assert
        assert row_nums == [2]

    def test_as_row_nums_returns_correct_array_for_multiple_groups(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        row_string = "_X_XX"

        # act
        row_nums = solver.as_row_nums(row_string)

        # assert
        assert row_nums == [1, 2]
