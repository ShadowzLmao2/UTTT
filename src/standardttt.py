from config import *
from functions import *
from solve_game import *
firstMove = True
standardGrid = (
    ([0]*3),
    ([0]*3),
    ([0]*3))

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

def checkWin(turn, x, y):
    global gameDone
    if y == 1 and standardGrid[x-1][y] == turn and standardGrid[x-1][y+1]:
        gameDone = True
    elif y == 2 and standardGrid[x-1][y-2] == turn and standardGrid[x-1][y]:
        gameDone = True
    elif y == 3 and standardGrid[x-1][y-2] == turn and standardGrid[x-1][y-3]:
        gameDone = True
    if x == 1 and standardGrid[x][y-1] == turn and standardGrid[x+1][y-1]:
        gameDone = True
    elif x == 2 and standardGrid[x-2][y-1] == turn and standardGrid[x][y-1]:
        gameDone = True
    elif x == 2 and y == 2:
        if (standardGrid[0][1] == turn and standardGrid[2][1] == turn) or (standardGrid[0][1] == turn and standardGrid[1][2] == turn):
            gameDone = True
        elif (standardGrid[0][0] == turn and standardGrid[2][2] == turn) or (standardGrid[2][0] == turn and standardGrid[0][2] == turn):
            gameDone = True
    return 

def makeMove():
    if gameDone:
        return
    print("x: ", end="")
    x = int(input())
    print("y: ", end="")
    y = int(input())
    if y < 1 or y > 3 or x < 1 or x > 3:
        print("Invalid location")
        makeMove()
    if firstMove:
        while (not x == 1 or y == 3) or (not x == 2 and y == 2):
            rotateSmall()
        firstMove = False
    if standardGrid[x-1][y-1] == 0:
        standardGrid[x-1][y-1] = turn
        switchPlayer()
        drawStandard()
        checkWin(turn, x, y)
    else:
        print("Invalid location")
        takeMove()