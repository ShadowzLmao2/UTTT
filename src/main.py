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
            print("-------------------")

def firstMove():
    print("x1: ", end="")
    x1 = int(input())
    if x1 < 1 or x1 > 3:
        print("Invalid location")
        return
    print("y1: ", end="")
    y1 = int(input())
    if y1 < 1 or y1 > 3:
        print("Invalid location")
        return
    print("x2: ", end="")
    x2 = int(input())
    if x2 < 1 or x2 > 3:
        print("Invalid location")
        return
    print("y2: ", end="")
    y2 = int(input())
    if y2 < 1 or y2 > 3:
        print("Invalid location")
        return
    totalX = (x1 - 1) * 3 + (x2 - 1)
    totalY = (y1 - 1) * 3 + (y2 - 1)
    if grid[totalX][totalY] == 0:
        grid[totalX][totalY] = 1
        drawGrid()

drawGrid()
firstMove()
def takeMove():
    return

