grid = (
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0])
x = 0
y = 0
gameDone = False
def drawGrid():
    for y in range(0,9):
        for x in range(0,9):
            print(grid[y][x], end="")
            if x == 2 or x == 5:
                print("| ", end="")
            if x < 8:
                print("|", end="")
            
        x = 0
        print("")
        if y == 2 or y == 5:
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
    global pastX
    global pastY
    pastX = (x1 - 1) * 3 + (x2 - 1)
    pastY = (y1 - 1) * 3 + (y2 - 1)
    if grid[pastY][pastX] == 0:
        grid[pastY][pastX] = 1
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
    global pastX
    pastX = pastX * 3 + (xInput - 1)
    global pastY
    pastY = pastY * 3 + (yInput - 1)
    if grid[pastY][pastX] == 0:
        grid[pastY][pastX] = 1
        pastX = xInput - 1
        pastY = xInput - 1
        drawGrid()

def checkBigWin(): #WIP
    return

def checkSmallWin(): #WIP
    smallWin = False
    if smallWin == True:
        checkBigWin()
    return