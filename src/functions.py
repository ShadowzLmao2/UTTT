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
    ([0]*3))
freeMove = False
pastMove = [2,2]
currentMove = [2,2]
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
        print("Invalid location")
        firstMove()
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
    takeMove()


def takeMove():
    if freeMove:
        print("x1: ", end="")
        initialX = int(input())
        print("y1: ", end="")
        initialY = int(input())
    print("x1: ", end="")
    xInput = int(input())
    print("y1: ", end="")
    yInput = int(input())
    if yInput < 1 or yInput > 3 or xInput < 1 or xInput > 3:
        badMove()
    if freeMove:
        currentMove[0] = (initialX - 1) * 3 + (xInput - 1)
        currentMove[1] = (initialY - 1) * 3 + (yInput - 1) 
    else:
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

def checkSmallWin(x,y,xInput,yInput,playerTurn):
    lastPlayedX = (x-1)*3+xInput
    lastPlayedY = (y-1)*3+yInput
    print(xInput)
    print(yInput)
    print(lastPlayedX)
    print(lastPlayedY)
    global smallWin
    smallWin = False
    #Top layer
    if yInput == 1:
        if grid[lastPlayedX][lastPlayedY+1] == playerTurn and grid[lastPlayedX][lastPlayedY+2]  == playerTurn:
            smallWin = True
    elif yInput == 2:
        if grid[lastPlayedX][lastPlayedY+1] == playerTurn and grid[lastPlayedX][lastPlayedY-1]  == playerTurn:
            smallWin = True
    elif yInput == 3:
        if grid[lastPlayedX][lastPlayedY-2] == playerTurn and grid[lastPlayedX][lastPlayedY-1]  == playerTurn:
            smallWin = True
    if xInput == 1:
        if grid[lastPlayedX+2][lastPlayedY] == playerTurn and grid[lastPlayedX+1][lastPlayedY]  == playerTurn:
            smallWin = True
    elif xInput == 2:
        if grid[lastPlayedX-1][lastPlayedY] == playerTurn and grid[lastPlayedX+1][lastPlayedY]  == playerTurn:
            smallWin = True
    else: #xInput = 3
        if grid[lastPlayedX-1][lastPlayedY] == playerTurn and grid[lastPlayedX-2][lastPlayedY]  == playerTurn:
            smallWin = True
    if smallWin == True:
        largeGrid[x][y] = playerTurn
        #Assign all in small grid as won
        for miniY in range(0,2):
            for miniX in range(0,2):
                grid[miniX+(x*3)][miniY+(y*3)] = playerTurn
        #checkBigWin()
    return
