from grid import Grid

test_grid = Grid(6)
print(test_grid)

test_grid.setup_puzzle()
print(test_grid)

for i in range(len(test_grid.row_strings)):
    row = test_grid.row_strings[i]
    print("ROW {}: {} = {}".format(i, test_grid.calculate_group_lengths(row), row))

for i in range(len(test_grid.row_strings)):
    column = test_grid.column_strings[i]
    print("COL {}: {} = {}".format(i, test_grid.calculate_group_lengths(column), column))
