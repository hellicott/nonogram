import unittest

from puzzle_solver import PuzzleSolver


class TestPuzzleReader(unittest.TestCase):

    def test_is_full_line_returns_true_when_full_line(self):
        # arrange
        solver = PuzzleSolver()
        solver.size = 10
        full_line = [4, 5]

        # act
        result = solver.is_full_line(full_line)

        # assert
        assert result == True

    def test_is_full_line_returns_false_when_not_full_line(self):
        # arrange
        solver = PuzzleSolver()
        solver.size = 10
        not_full_line = [4, 4]

        # act
        result = solver.is_full_line(not_full_line)

        # assert
        assert result == False
