from SudokuAlgorithm import SudokuAlgorithm

sudokuBoard = [
                [0,4,0,8,0,5,2,0,0],
                [0,2,0,0,4,0,0,5,0],
                [5,0,0,0,0,0,0,0,4],
                [0,9,0,0,0,3,1,2,0],
                [1,0,6,0,7,8,0,0,3],
                [3,7,0,9,0,4,0,8,0],
                [0,0,0,0,0,6,7,0,0],
                [0,0,8,3,5,9,0,1,0],
                [0,1,9,0,0,7,6,0,0]
        ]

board = SudokuAlgorithm()
board.solve(0 , 0 , sudokuBoard)
board.printBoard(sudokuBoard)