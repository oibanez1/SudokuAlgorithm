# SudokuAlgorithm
Rules of Soduku: Fill in empty cells with the numbers 1-9 without repeating any within a row, column, or block. There are 9 blocks and each block is a 3x3 area starting from top left.

To run this program - python and pygame must be installed

Solves any sudoku board using backtracking algorithm. The backtracking algorithm tests a number and if it is valid it will continue on to the next cell, if it is not valid then
it will test the next number until a possible solution is valid. If at any point no possible solutions are valid it will backtrack, or delete, previous input and try another solution.
