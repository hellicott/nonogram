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
        row_nums = solver._as_row_nums(row_string)

        # assert
        assert row_nums == [2]

    def test_as_row_nums_returns_correct_array_for_multiple_groups(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        row_string = "_X_XX"

        # act
        row_nums = solver._as_row_nums(row_string)

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

    def test_solve_row_returns_solved_row(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        row_string = ".X.XX"
        row_nums = [2, 2]

        # act
        row = solver.solve_row(row_string, row_nums)

        # assert
        assert row == "XX_XX"

    def test_calculate_percentage_returns_correct_percentage(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        row_nums = [2, 2]
        row_string = "X..XX"

        # act
        percentage = solver.calculate_percentage(row_string, row_nums)

        # assert
        assert percentage == 50

    def test_fill_row_with_random_squares_returns_acceptable_row_string(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        row_string = "X..X."
        percentage = 20

        # act
        new_row_string = solver.fill_row_with_random_squares(percentage, row_string)

        # assert
        assert new_row_string.count("X") + new_row_string.count("_") == 5 \
            and len(new_row_string) == 5

    def test_get_numbers_as_line_returns_correct_line(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        numbers = [2, 1]

        # act
        line = solver.get_numbers_as_line(numbers)

        # assert
        assert line == [1, 1, 0, 1, 0]

    def test_find_definite_squares_in_line_returns_correct_squares(self):
        # arrange
        reader = mock.create_autospec(PuzzleReader)
        reader.get_row_and_column_numbers.return_value = "value 1", "value 2"
        solver = Solver(Grid(5), reader)
        numbers = [2, 1]

        # act
        definite = solver.find_definite_squares_in_line(numbers)

        # assert
        assert definite == ".X..."

    def test_fill_definite_squares_in_row(self):
        # arrange
        path = r"/home/hannah/Documents/FunProjects/Challenges/nonogram/test_nonogram_5x5.json"
        reader = PuzzleReader(path)
        solver = Solver(Grid(5), reader)

        # act
        solver.fill_definite_squares_in_row()

        # assert
        assert solver.grid.get_row_as_string(4) == "..X.."

    def test_fill_definite_squares_in_column(self):
        # arrange
        path = r"/home/hannah/Documents/FunProjects/Challenges/nonogram/test_nonogram_5x5.json"
        reader = PuzzleReader(path)
        solver = Solver(Grid(5), reader)

        # act
        solver.fill_definite_squares_in_column()

        # assert
        assert solver.grid.get_column_as_string(4) == ".X.X."
