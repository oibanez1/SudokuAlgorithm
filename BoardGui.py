from SudokuAlgorithm import SudokuAlgorithm
from copy import copy , deepcopy
import pygame , sys
pygame.init()

windowSize = 600 , 600
white = 255 , 255 , 255
black = 0 , 0 , 0
red = 255 , 0 , 0

screen = pygame.display.set_mode(windowSize)
screen.fill(white)
pygame.display.set_caption('Sudoku')

x = 0
y = 0
#end
a = 600
b = 504
across = 56
horziontal = 67
#original board
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
#obj of class named SudokuAlgo...
board = SudokuAlgorithm()

#copy of original board and solved
sudokuSolved = deepcopy(sudokuBoard) 
board.solve(0 , 0 , sudokuSolved)

#Draws grid lines
def drawGrid():
    for line in range(10):
        if line % 3 == 0:
            thickness = 4
        else:
            thickness = 1   
        pygame.draw.line(screen , black , (x , line * across) , (a , line * across) , thickness)   
        pygame.draw.line(screen , black , (line * horziontal , y) , (line * horziontal , b) , thickness)

#Draws numbers present
def printBoard(board):
    num = pygame.font.Font('freesansbold.ttf' , 20)
    length = len(board)
    y_coord = 16
    for x in range(length):
        x_coord = 25
        for y in range(length):
            #if number == 0, do nothing and continue
            if board[x][y] == 0:
                x_coord += 65
                continue
            if board[y] == 6 or 7 or 8:
                x_coord += 4
            #Draws numbers on screen    
            text = num.render(str(board[x][y]) , True , black)
            screen.blit(text , [x_coord , y_coord])  
            x_coord += 65    
        y_coord += 55

printBoard(sudokuBoard)
drawGrid()  
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x_index = int(pos[1] / 55)
            y_index = int(pos[0] / 65)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = 1
            if event.key == pygame.K_2:
                key = 2
            if event.key == pygame.K_3:
                key = 3
            if event.key == pygame.K_4:
                key = 4
            if event.key == pygame.K_5:
                key = 5
            if event.key == pygame.K_6:
                key = 6
            if event.key == pygame.K_7:
                key = 7
            if event.key == pygame.K_8:
                key = 8
            if event.key == pygame.K_9:
                key = 9  
            inputNumber = str(key)
            number = pygame.font.Font('freesansbold.ttf' , 20)
            convertNum = number.render(inputNumber , True , black)
            screen.blit(convertNum , pos)
            if event.key == pygame.K_RETURN:
                if inputNumber != str(sudokuSolved[x_index][y_index]):
                    print('Wrong')
                    pygame.draw.circle(screen , white , pos , 18 , 15)
                else:
                    print('Correct')
                    #screen.blit(convertNum , pos)
                    sudokuBoard[x_index][y_index] = int(inputNumber)
                if sudokuBoard == sudokuSolved:
                    print('Congrats, you finished')                 
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.update()
pygame.quit()

