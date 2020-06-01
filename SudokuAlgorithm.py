class SudokuAlgorithm:

    def solve(self , row , col , board):
        #base case
        if col == len(board):
            col = 0
            row += 1

        if row == len(board):
            return True

        #if number is not 0 -> num is present -> go to next cell
        if board[row][col] != 0:
            return self.solve(row , col + 1 , board)

        #iterate through one row, 1-10
        for inputVal in range(1 , 10):
            #if number adheres to constraints -> current indice will equal that number
            if self.validPlacement(row , col , board , inputVal):
                board[row][col] = inputVal
                #go to next cell if possible
                if self.solve(row , col + 1 , board):
                    return True
                #validPlacement = false -> set back to 0 and try again    
                else:
                    board[row][col] = 0

        return False

    def validPlacement(self , row , col , board , inputVal):
        rowIndex = int(row / 3)    #index 0-2 -> 0    3-5 -> 1   6-8 -> 2
        colIndex = int(col / 3)    #index 0-2 -> 0    3-5 -> 1   6-8 -> 2

        topLeftRow = rowIndex * 3
        topLeftCol = colIndex * 3
        
        #iterate through row to see if inputVal is in row
        for x in board[row]:
            if x == inputVal:
                return False

        #iterate through column to see if inputVal is in column
        for x in range(0 , 9):
            if board[x][col] == inputVal:
                return False

        #iterate through a block(specific 3x3 area) to see if inputVal is in block
        for x in range(3):
            for y in range(3):
                if board[topLeftRow + y][topLeftCol + y] == inputVal:
                    return False
        return True        

    #prints whole 2d array
    def printBoard(self , board):
        for x in board:
            print()
            for y in x:
                print(y , end = " ")

    