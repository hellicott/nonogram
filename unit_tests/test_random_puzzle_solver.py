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

    def test_is_row_solved_returns_true_when_row_matches_row_nums(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        row_string = "_X_XX"
        row_nums = [1, 2]

        # act
        result = solver.is_row_solved(row_string, row_nums)

        # assert
        assert result is True

    def test_is_row_solved_returns_false_when_row_does_not_match_row_nums(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        row_string = "_X_XX"
        row_nums = [1, 2, 1]

        # act
        result = solver.is_row_solved(row_string, row_nums)

        # assert
        assert result is False