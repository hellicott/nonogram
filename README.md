# nonogram solver
First attempt at a nonogram solver

The approach is a 'slightly better than random' algorithm

It starts by finding the squares which definitely must be filled by checking each row and column

It then goes through each row and calculates the number of squares yet to be filled, and the number of squares that need to be filled and randomly fills the squares with that ratio

Unfortunately this doesn't work at solving the problem as it is only checking the rows, not the columns. It therefore allows XXX__ to count as being solved, even if the actual solution is \_XXX_
