from standardttt import drawStandard

def isGameEndable(): 
    if countBlankSpaces() == 1:
        fillStandardGrid()
        drawStandard()
    return

def countBlankSpaces():
    count = 0
    global standardGrid
    for y in range(0,3):
        for x in range(0,3):
            if standardGrid[x][y] == 0:
                count+=1
    return count
    
def fillStandardGrid():
    for y in range(0,3):
        for x in range(0,3):
            if standardGrid[x][y] == 0:
                standardGrid[x][y] = turn