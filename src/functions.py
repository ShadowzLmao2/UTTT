from config import simplify_table
from solve_game import *
from import_game import *
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
    ([0]*3))
freeMove = True
pastMoveX = 2
pastMoveY = 2
actualMoveX = 2
actualMoveY = 2
recentMoveX = 2
recentMoveY = 2
playerTurn = 1
gameDone = False
def drawGrid():
    for y in range(0,9):
        for x in range(0,9):
            if grid[x][y] == 0:
                print("-", end="")
            elif grid[x][y] == 1:
                print("X", end="")
            else:
                print("O", end="")
            if (x == 2 or x == 5) and not simplify_table:
                print("| ", end="")
            if x < 8 and not simplify_table:
                print("|", end="")
        print("")
        if (y == 2 or y == 5) and not simplify_table:
            print("---------------------")

def openMove():
    print("x1: ", end="")
    x1 = int(input())
    print("y1: ", end="")
    y1 = int(input())
    print("x2: ", end="")
    x2 = int(input())
    print("y2: ", end="")
    y2 = int(input())
    if y2 < 1 or y2 > 3 or x2 < 1 or x2 > 3 or y1 < 1 or y1 > 3 or x1 < 1 or x1 > 3:
        print("Invalid location")
        openMove()
    actualMoveX = (x1 - 1) * 3 + (x2 - 1)
    actualMoveY = (y1 - 1) * 3 + (y2 - 1)
    if grid[actualMoveX][actualMoveY] == 0:
        grid[actualMoveX][actualMoveY] = playerTurn
        freeMove = False
        global pastMoveY
        global pastMoveX
        pastMoveX = x2
        pastMoveY = y2
        checkSmallWin(pastMoveX,pastMoveY,x2,y2,playerTurn)
        switchPlayer()
        drawGrid()
        if not gameDone:
            shouldGiveFreeMove(pastMoveX,pastMoveY)
    else: 
        print("Invalid location")
        openMove()

def badMove():
    print("Invalid location")
    takeMove()

def takeMove():
    print("x: ", end="")
    xInput = int(input())
    print("y: ", end="")
    yInput = int(input())
    if yInput < 1 or yInput > 3 or xInput < 1 or xInput > 3:
        badMove()
    global pastMoveX
    global pastMoveY
    recentMoveX = pastMoveX * 3 - 4 + xInput
    recentMoveY = pastMoveY * 3 - 4 + yInput
    if grid[recentMoveX][recentMoveY] == 0:
        grid[recentMoveX][recentMoveY] = playerTurn
        checkSmallWin(pastMoveX,pastMoveY,xInput,yInput,playerTurn)
        pastMoveX = xInput
        pastMoveY = yInput
        switchPlayer()
        drawGrid()
        shouldGiveFreeMove(xInput,yInput)
    else:
        badMove()

def switchPlayer():
    global playerTurn
    if playerTurn == 1:
        playerTurn = 2
    else:
        playerTurn = 1
    return
    
def checkBigWin(x,y,playerTurn): #x and y are based on largeGrid coords, and can be 0, 1, or 2
    bigWin = False
    global gameDone
    #Horizontal Win
    if y == 0 and largeGrid[x][y+1] == playerTurn and largeGrid[x][y+2] == playerTurn:
        bigWin = True
    if y == 1 and largeGrid[x][y+1] == playerTurn and largeGrid[x][y-1] == playerTurn:
        bigWin = True
    if y == 2 and largeGrid[x][y-2] == playerTurn and largeGrid[x][y-1] == playerTurn:
        bigWin = True
    #Vertical Win
    if x == 0 and largeGrid[x+1][y] == playerTurn and largeGrid[x+2][y] == playerTurn:
        bigWin = True
    if x == 1 and largeGrid[x+1][y] == playerTurn and largeGrid[x-1][y] == playerTurn:
        bigWin = True
    if x == 2 and largeGrid[x-2][y] == playerTurn and largeGrid[x-1][y] == playerTurn:
        bigWin = True
    #Diagonals
    if largeGrid[1][1] == playerTurn and (largeGrid[0][0] == playerTurn and largeGrid[2][2] == playerTurn) or (largeGrid[0][2] == playerTurn and largeGrid[2][0] == playerTurn):
        bigWin = True
    if bigWin:
        if playerTurn == 1:
            print("Game Over, Winner is: X")
        else: 
            print("Game Over, Winner is: O")
        gameDone = True
    return

def checkSmallWin(x,y,xInput,yInput,playerTurn):
    lastPlayedX = x*3-4+xInput
    lastPlayedY = y*3-4+yInput
    #Vertical Win
    if yInput == 1 and grid[lastPlayedX][lastPlayedY+1] == playerTurn and grid[lastPlayedX][lastPlayedY+2]  == playerTurn:
            confirmSmallWin(x,y,playerTurn)
    if yInput == 2 and grid[lastPlayedX][lastPlayedY+1] == playerTurn and grid[lastPlayedX][lastPlayedY-1]  == playerTurn:
            confirmSmallWin(x,y,playerTurn)
    if yInput == 3 and grid[lastPlayedX][lastPlayedY-2] == playerTurn and grid[lastPlayedX][lastPlayedY-1]  == playerTurn:
            confirmSmallWin(x,y,playerTurn)
    #Horizontal Win
    if xInput == 1 and grid[lastPlayedX+2][lastPlayedY] == playerTurn and grid[lastPlayedX+1][lastPlayedY]  == playerTurn:
            confirmSmallWin(x,y,playerTurn)
    if xInput == 2 and grid[lastPlayedX-1][lastPlayedY] == playerTurn and grid[lastPlayedX+1][lastPlayedY]  == playerTurn:
            confirmSmallWin(x,y,playerTurn)
    if xInput == 3 and grid[lastPlayedX-1][lastPlayedY] == playerTurn and grid[lastPlayedX-2][lastPlayedY]  == playerTurn:
            confirmSmallWin(x,y,playerTurn)
    #Diagonal Win
    if   yInput == 2 and xInput == 2:
        if grid[lastPlayedX+1][lastPlayedY+1] == playerTurn and grid[lastPlayedX-1][lastPlayedY-1] == playerTurn:
            confirmSmallWin(x,y,playerTurn)
        if grid[lastPlayedX+1][lastPlayedY-1] == playerTurn and grid[lastPlayedX-1][lastPlayedY+1] == playerTurn:
            confirmSmallWin(x,y,playerTurn)
    #Check if middle is correct then looks at the opposite corner
    if grid[x*3-2][y*3-2] != playerTurn:
        return
    if xInput == 1 and yInput == 1 and grid[lastPlayedX+2][lastPlayedY+2] == playerTurn:
        confirmSmallWin(x,y,playerTurn)
    if xInput == 1 and yInput == 3 and grid[lastPlayedX+2][lastPlayedY-2] == playerTurn:
        confirmSmallWin(x,y,playerTurn)
    if xInput == 3 and yInput == 1 and grid[lastPlayedX-2][lastPlayedY+2] == playerTurn:
        confirmSmallWin(x,y,playerTurn)
    if xInput == 3 and yInput == 3 and grid[lastPlayedX-2][lastPlayedY-2] == playerTurn:
        confirmSmallWin(x,y,playerTurn)
    return

def confirmSmallWin(x,y,playerTurn):
    largeGrid[x-1][y-1] = playerTurn
    for miniY in range(0,3):
        for miniX in range(0,3):
            grid[miniX+(x*3-3)][miniY+(y*3-3)] = playerTurn
    checkBigWin(x-1,y-1,playerTurn)
    return

def shouldGiveFreeMove(pastX,pastY):
    if largeGrid[pastX-1][pastY-1] != 0:
        openMove()
    return
