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
            #print(grid[y][x], end="")
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
    if x1 < 1 or x1 > 3:
        print("Invalid location")
        firstMove()
    print("y1: ", end="")
    y1 = int(input())
    if y1 < 1 or y1 > 3:
        print("Invalid location")
        firstMove()
    print("x2: ", end="")
    x2 = int(input())
    if x2 < 1 or x2 > 3:
        print("Invalid location")
        firstMove()
    print("y2: ", end="")
    y2 = int(input())
    if y2 < 1 or y2 > 3:
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

def takeMove():
    print("x1: ", end="")
    xInput = int(input())
    if xInput < 1 or xInput > 3:
        print("Invalid location")
        takeMove()
    print("y1: ", end="")
    yInput = int(input())
    if yInput < 1 or yInput > 3:
        print("Invalid location")
        takeMove()
    currentMove[0] = (pastMove[0] - 1) * 3 + (xInput - 1)
    currentMove[1] = (pastMove[1] - 1) * 3 + (yInput - 1) 
    if grid[currentMove[1]][currentMove[0]] == 0:
        grid[currentMove[1]][currentMove[0]] = playerTurn
        pastMove[0] = xInput
        pastMove[1] = yInput
        switchPlayer()
        drawGrid()
    else:
        print("Spot already taken")
        takeMove()

def switchPlayer():
    global playerTurn
    if playerTurn == 1:
        playerTurn = 2
    else:
        playerTurn = 1
    return
    
def checkBigWin(): #WIP
    return

def checkSmallWin(): #WIP
    smallWin = False
    if smallWin == True:
        checkBigWin()
    return