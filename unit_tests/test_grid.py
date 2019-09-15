import unittest

from grid import Grid


class TestPuzzleReader(unittest.TestCase):
    def test_build_empty_grid(self):
        # arrange
        grid_size = 10
        grid = Grid(grid_size)

        # act
        empty_grid = grid._build_empty_grid()

        # assert
        assert len(empty_grid) == grid_size

    def test_insert_value_to_grid_changes_specified_row(self):
        # arrange
        grid = Grid(10)
        value = 1
        row_num = 3
        col_num = 5

        # act
        grid.insert_value_to_grid(value, row_num, col_num)

        # assert
        assert grid.grid[row_num][col_num] == value

    def test_insert_value_to_grid_does_not_change_unspecified_row(self):
        # arrange
        grid = Grid(10)
        value = 1
        row_num = 3
        col_num = 5

        # act
        grid.insert_value_to_grid(value, row_num, col_num)

        # assert
        assert grid.grid[row_num+1][col_num] == 0

    def test_get_row_as_string(self):
        # arrange
        row_num = 3
        grid = Grid(10)
        grid.insert_value_to_grid(1, row_num, 0)

        # act
        row_string = grid.get_row_as_string(row_num)

        # assert
        assert row_string == ("1" + "0" * 9)

    def test_get_row_as_string(self):
        # arrange
        col_num = 4
        grid = Grid(10)
        grid.insert_value_to_grid(1, 0, col_num)

        # act
        row_string = grid.get_column_as_string(col_num)

        # assert
        assert row_string == ("1" + "0" * 9)
