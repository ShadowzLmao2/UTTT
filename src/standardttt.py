from config import *
from functions import *
from convert_matrix import rotateSmall
firstMove = True
filledXY = [0,0]
gameDone = False
pTurn = 1
standardGrid = (
    ([0]*3),
    ([0]*3),
    ([0]*3))
playedMoves = (([0]*9),([0]*9))
currentMove = 0

def drawStandard():
    for y in range(0,3):
        for x in range(0,3):
            if standardGrid[x][y] == 0:
                print("-", end="")
            elif standardGrid[x][y] == 1 and not x_and_o_numbers:
                print("X", end="")
            elif standardGrid[x][y] == 2 and not x_and_o_numbers:
                print("O", end="")
            elif standardGrid[x][y] == 2 and x_and_o_numbers:
                print("X", end="")
            else:
                print("O", end="")
            if x == 2:
                print("")
            else:
                print("|", end="")

def checkWin(pTurn, x, y):
    global gameDone
    if y == 1 and standardGrid[x-1][1] == pTurn and standardGrid[x-1][2] == pTurn:
        gameDone = True
    elif y == 2 and standardGrid[x-1][0] == pTurn and standardGrid[x-1][2] == pTurn:
        gameDone = True
    elif y == 3 and standardGrid[x-1][0] == pTurn and standardGrid[x-1][1] == pTurn:
        gameDone = True
    if x == 1 and standardGrid[1][y-1] == pTurn and standardGrid[2][y-1] == pTurn:
        gameDone = True
    elif x == 2 and standardGrid[0][y-1] == pTurn and standardGrid[2][y-1] == pTurn:
        gameDone = True
    elif x == 3 and standardGrid[0][y-1] == pTurn and standardGrid[1][y-1] == pTurn:
        gameDone = True
    elif x == 2 and y == 2:
        if (standardGrid[0][0] == pTurn and standardGrid[2][2] == pTurn) or (standardGrid[0][2] == pTurn and standardGrid[2][0] == pTurn):
            gameDone = True
    if gameDone == True:
        if pTurn == 1:
            print("Game Over: X win")
        elif pTurn == 2:
            print("Game Over: O win")
    elif countBlankSpaces() == 0:
        print("Game Over: Draw")
    return 

def makeMove():
    print("x: ", end="")
    x = int(input())
    print("y: ", end="")
    y = int(input())
    if y < 1 or y > 3 or x < 1 or x > 3:
        print("Invalid location")
        makeMove()
    global pTurn
    if standardGrid[x-1][y-1] == 0:
        standardGrid[x-1][y-1] = pTurn
        drawStandard()
        checkWin(pTurn, x, y)
        switch3x3Player()
        isGameWinnable()
        if gameDone:
            return
    else:
        print("Invalid location")
        makeMove()

def switch3x3Player():
    global pTurn
    if pTurn == 1:
        pTurn = 2
    else:
        pTurn = 1
    return
    
def playStandardTTT():
    drawStandard()
    while gameDone == False:
        makeMove()
    if display_moves:
        showMoves()
    return

def isGameWinnable(): 
    global filledXY
    if countBlankSpaces() == 1:
        fillStandardGrid()
        drawStandard()
        checkWin(pTurn, filledXY[0] + 1, filledXY[1] + 1)
    return

def countBlankSpaces():
    count = 0
    for y in range(0,3):
        for x in range(0,3):
            if standardGrid[x][y] == 0:
                count+=1
    return count
    
def fillStandardGrid():
    global filledXY
    for y in range(0,3):
        for x in range(0,3):
            if standardGrid[x][y] == 0:
                standardGrid[x][y] = turn
                filledXY[0] = x
                filledXY[1] = y
                print()
                return
    return

def showMoves():
    for x in range(0,9):
        print( "(", playedMoves[x,0], ", ", playedMoves[x,1], ")" )
    return

playStandardTTT()