from config import *
#from solve_game import *
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
largeGrid = ([0]*9)
freeMove = True
pastMoveX = 2
pastMoveY = 2
actualMoveX = 2
actualMoveY = 2
recentMoveX = 2
recentMoveY = 2
turn = 1
gameDone = False

def drawGrid():
    for y in range(0,9):
        for x in range(0,9):
            if grid[x][y] == 0:
                print("-", end="")
            elif grid[x][y] == 1 and not x_and_o_numbers:
                print("X", end="")
            elif grid[x][y] == 2 and not x_and_o_numbers:
                print("O", end="")
            elif grid[x][y] == 2 and x_and_o_numbers:
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
        grid[actualMoveX][actualMoveY] = turn
        freeMove = False
        global pastMoveY
        global pastMoveX
        checkSmallWin(x1,y1,x2,y2,turn)
        pastMoveX = x2
        pastMoveY = y2
        switchPlayer()
        if not gameDone:
            drawGrid()
            shouldGiveFreeMove(pastMoveX,pastMoveY)
    else: 
        print("Invalid location")
        openMove()

def takeMove():
    if gameDone:
        return
    print("x: ", end="")
    xInput = int(input())
    print("y: ", end="")
    yInput = int(input())
    if yInput < 1 or yInput > 3 or xInput < 1 or xInput > 3:
        print("Invalid location")
        takeMove()
    global pastMoveX
    global pastMoveY
    recentMoveX = pastMoveX * 3 - 4 + xInput
    recentMoveY = pastMoveY * 3 - 4 + yInput
    if grid[recentMoveX][recentMoveY] == 0:
        grid[recentMoveX][recentMoveY] = turn
        checkSmallWin(pastMoveX,pastMoveY,xInput,yInput,turn)
        pastMoveX = xInput
        pastMoveY = yInput
        switchPlayer()
        drawGrid()
        shouldGiveFreeMove(xInput,yInput)
    else:
        print("Invalid location")
        takeMove()

def switchPlayer():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1
    return
    
def checkBigWin(x,y,turn): #x and y are based on largeGrid coords, and can be 0, 1, or 2
    bigWin = False
    global gameDone
    #Horizontal Win
    if y == 0 and largeGrid[x+(y+1)*3] == turn and largeGrid[x+(y-1)*3] == turn:
        bigWin = True
    elif y == 1 and largeGrid[x+(y+1)*3] == turn and largeGrid[x+(y-1)*3] == turn:
        bigWin = True
    elif y == 2 and largeGrid[x+(y+-2)*3] == turn and largeGrid[x+(y-1)*3] == turn:
        bigWin = True
    #Vertical Win
    if x == 0 and largeGrid[x+1+y*3] == turn and largeGrid[x+2+y*3] == turn:
        bigWin = True
    elif x == 1 and largeGrid[x+1+y*3] == turn and largeGrid[x-1+y*3] == turn:
        bigWin = True
    elif x == 2 and largeGrid[x-2+y*3] == turn and largeGrid[x-1+y*3] == turn:
        bigWin = True
    #Diagonals
    if largeGrid[4] == turn and (largeGrid[0] == turn and largeGrid[8] == turn) or (largeGrid[6] == turn and largeGrid[2] == turn):
        bigWin = True
    if bigWin:
        if turn == 1:
            print("Game Over, Winner is: X")
        else: 
            print("Game Over, Winner is: O")
        gameDone = True
    return

def checkSmallWin(x,y,xInput,yInput,turn):
    if gameDone:
        return
    lastPlayedX = x*3-4+xInput
    lastPlayedY = y*3-4+yInput
    inverseY = 4 - yInput
    inverseX = 4 - xInput
    #Vertical Win
    if yInput == 1 and grid[lastPlayedX][lastPlayedY+1] == turn and grid[lastPlayedX][lastPlayedY+2]  == turn:
        confirmSmallWin(x,y,turn)
    elif yInput == 2 and grid[lastPlayedX][lastPlayedY+1] == turn and grid[lastPlayedX][lastPlayedY-1]  == turn:
        confirmSmallWin(x,y,turn)
    elif yInput == 3 and grid[lastPlayedX][lastPlayedY-2] == turn and grid[lastPlayedX][lastPlayedY-1]  == turn:
        confirmSmallWin(x,y,turn)
    #Horizontal Win
    if xInput == 1 and grid[lastPlayedX+2][lastPlayedY] == turn and grid[lastPlayedX+1][lastPlayedY]  == turn:
        confirmSmallWin(x,y,turn)
    elif xInput == 2 and grid[lastPlayedX-1][lastPlayedY] == turn and grid[lastPlayedX+1][lastPlayedY]  == turn:
        confirmSmallWin(x,y,turn)
    elif xInput == 3 and grid[lastPlayedX-1][lastPlayedY] == turn and grid[lastPlayedX-2][lastPlayedY]  == turn:
        confirmSmallWin(x,y,turn)
    #Diagonal Win
    if yInput == 2 and xInput == 2:
        if grid[lastPlayedX+1][lastPlayedY+1] == turn and grid[lastPlayedX-1][lastPlayedY-1] == turn:
            confirmSmallWin(x,y,turn)
        elif grid[lastPlayedX+1][lastPlayedY-1] == turn and grid[lastPlayedX-1][lastPlayedY+1] == turn:
            confirmSmallWin(x,y,turn)
    elif (yInput == 1 or yInput == 3) and (xInput == 1 or xInput == 3):
        if grid[x*3-2][y*3-2] and grid[inverseX+x*3-3][inverseY+y*3-3]:
            confirmSmallWin(x,y,turn)
    #Check if middle is correct then looks at the opposite corner
    if grid[x*3-2][y*3-2] == turn:
        if xInput == 1 and yInput == 1 and grid[lastPlayedX+2][lastPlayedY+2] == turn:
            confirmSmallWin(x,y,turn)
        elif xInput == 1 and yInput == 3 and grid[lastPlayedX+2][lastPlayedY-2] == turn:
            confirmSmallWin(x,y,turn)
        elif xInput == 3 and yInput == 1 and grid[lastPlayedX-2][lastPlayedY+2] == turn:
            confirmSmallWin(x,y,turn)
        elif xInput == 3 and yInput == 3 and grid[lastPlayedX-2][lastPlayedY-2] == turn:
            confirmSmallWin(x,y,turn)
    return

def confirmSmallWin(x,y,turn):
    if gameDone:
        return
    largeGrid[x-1+(y-1)*3] = turn
    for miniY in range(0,3):
        for miniX in range(0,3):
            grid[miniX+(x*3-3)][miniY+(y*3-3)] = turn
    checkBigWin(x-1,y-1,turn)
    return

def shouldGiveFreeMove(pastX,pastY):
    if largeGrid[pastX-1+(pastY-1)*3] != 0:
        openMove()
    return
