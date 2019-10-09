

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = self._build_empty_grid()

    def _build_empty_grid(self):
        grid = [["."] * self.size for _ in range(self.size)]
        return grid

    def insert_row_to_grid(self, row, row_num):
        col_num = 0
        for value in row:
            if value == "X":
                self.insert_value_to_grid(value, row_num, col_num)
            col_num += 1

    def insert_column_to_grid(self, column, column_num):
        row_num = 0
        for value in column:
            if value == "X":
                self.insert_value_to_grid(value, row_num, column_num)
            row_num += 1

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

    def calculate_line_numbers(self, row=True):
        all_line_nums = []
        for line_num in range(self.size):
            if row:
                line_string = self.get_row_as_string(line_num)
            else:
                line_string = self.get_column_as_string(line_num)
            line_string = line_string.split("_")
            row_nums = [x for x in line_string if x]
            all_line_nums.append(row_nums)
        return all_line_nums

    def __str__(self):
        printed_grid = ""
        for i in range(self.size):
            printed_grid = printed_grid + self.get_row_as_string(i) + "\n"
        return printed_grid
