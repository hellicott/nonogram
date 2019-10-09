import unittest
from unittest import mock

from grid import Grid
from puzzle_solver import PuzzleSolver


class TestPuzzleReader(unittest.TestCase):

    def test_is_full_line_returns_true_when_full_line(self):
        # arrange
        solver = PuzzleSolver(Grid(10))
        solver.size = 10
        full_line = [4, 5]

        # act
        result = solver.is_full_line(full_line)

        # assert
        assert result is True

    def test_is_full_line_returns_false_when_not_full_line(self):
        # arrange
        solver = PuzzleSolver(Grid(10))
        solver.size = 10
        not_full_line = [4, 4]

        # act
        result = solver.is_full_line(not_full_line)

        # assert
        assert result is False

    def test_get_numbers_as_line_returns_correct_line_when_given_full_line(self):
        # arrange
        numbers = [4, 5]
        grid = mock.create_autospec(Grid(10))
        solver = PuzzleSolver(grid)
        solver.size = 10

        # act
        line = solver.get_numbers_as_line(numbers)

        # assert
        assert line == [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]

    def test_get_numbers_as_line_returns_correct_line_when_given_short_line(self):
        # arrange
        numbers = [4, 4]
        grid = mock.create_autospec(Grid(10))
        solver = PuzzleSolver(grid)
        solver.size = 10

        # act
        line = solver.get_numbers_as_line(numbers)

        # assert
        assert line == [1, 1, 1, 1, 0, 1, 1, 1, 1, 0]
