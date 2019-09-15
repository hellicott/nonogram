

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = self._build_empty_grid()

    def _build_empty_grid(self):
        grid = [[0] * self.size for _ in range(self.size)]
        return grid

    def insert_value_to_grid(self, value, row, column):
        self.grid[row][column] = value

    def get_row_as_string(self, row_num):
        row = self.grid[row_num]
        return ''.join(str(x) for x in row)

    def get_column_as_string(self, column_num):
        column = []
        for row in self.grid:
            column.append(row[column_num])
        return ''.join(str(x) for x in column)
