from config import *
grid = (
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9))
largeGrid = (
    ([0]*3),
    ([0]*3),
    ([0]*3),)

pastMove = [0,0]
currentMove = [0,0]
playerTurn = 1
gameDone = False
def drawGrid():
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x] == 0:
                print("-", end="")
            elif grid[y][x] == 1:
                print("X", end="")
            else:
                print("0", end="")
            if (x == 2 or x == 5) and not simplify_table:
                print("| ", end="")
            if x < 8 and not simplify_table:
                print("|", end="")
        x = 0
        print("")
        if (y == 2 or y == 5) and not simplify_table:
            print("---------------------")

def firstMove():
    print("x1: ", end="")
    x1 = int(input())
    print("y1: ", end="")
    y1 = int(input())
    print("x2: ", end="")
    x2 = int(input())
    print("y2: ", end="")
    y2 = int(input())
    if y2 < 1 or y2 > 3 or x2 < 1 or x2 > 3:
        badMove()
    pastMove[0] = (x1 - 1) * 3 + (x2 - 1)
    pastMove[1] = (y1 - 1) * 3 + (y2 - 1)
    if grid[pastMove[1]][pastMove[0]] == 0:
        grid[pastMove[1]][pastMove[0]] = 1
        pastMove[0] = x2
        pastMove[1] = y2
        switchPlayer()
        drawGrid()

def badMove():
    print("Invalid location")
    firstMove()


def takeMove():
    print("x1: ", end="")
    xInput = int(input())
    print("y1: ", end="")
    yInput = int(input())
    if yInput < 1 or yInput > 3 or xInput < 1 or xInput > 3:
        badMove()
    currentMove[0] = (pastMove[0] - 1) * 3 + (xInput - 1)
    currentMove[1] = (pastMove[1] - 1) * 3 + (yInput - 1) 
    if grid[currentMove[1]][currentMove[0]] == 0:
        grid[currentMove[1]][currentMove[0]] = playerTurn
        checkSmallWin(pastMove[0],pastMove[1],xInput,yInput,playerTurn)
        pastMove[0] = xInput
        pastMove[1] = yInput
        switchPlayer()
        drawGrid()
    else:
        badMove()

def switchPlayer():
    global playerTurn
    if playerTurn == 1:
        playerTurn = 2
    else:
        playerTurn = 1
    return
    
def checkBigWin(): #WIP
    return

def checkSmallWin(x,y,xInput,yInput,playerTurn): #WIP
    lastPlayedX = x*3+xInput
    lastPlayedY = y*3+yInput
    #if x != 2 and y != 2:
        #smallWin = True
    if grid[lastPlayedX+2][lastPlayedY] == playerTurn and grid[lastPlayedX+1][lastPlayedY] == playerTurn and lastPlayedX == 1:
        smallWin = True
    if grid[lastPlayedX+1][lastPlayedY] == playerTurn and grid[lastPlayedX-1][lastPlayedY] == playerTurn and lastPlayedX == 2:
        smallWin = True
    if grid[lastPlayedX-2][lastPlayedY] == playerTurn and grid[lastPlayedX-1][lastPlayedY] == playerTurn and lastPlayedX == 3:
        smallWin = True
    if grid[lastPlayedX][lastPlayedY+2] == playerTurn and grid[lastPlayedX][lastPlayedX+1] == playerTurn and lastPlayedY == 1:
        smallWin = True
    if grid[lastPlayedX][lastPlayedY+1] == playerTurn and grid[lastPlayedX][lastPlayedX-1] == playerTurn and lastPlayedY == 2:
        smallWin = True
    if grid[lastPlayedX][lastPlayedY-2] == playerTurn and grid[lastPlayedX][lastPlayedX-1] == playerTurn and lastPlayedY == 3:
        smallWin = True
    if smallWin == True:
        largeGrid[x][y] = playerTurn
        checkBigWin()
    return
