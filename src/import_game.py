from functions import *
def getBigBoard():
    return

def getSmallerBoards():
    return

def getEntireBoard():
    confirmSmallWin(1,1,1)
    return

def askForBoardState():
    for y in range (1,4):
        for x in range (1,4):
            print("Which player won x", x, "and y", y, "?")
            largeGrid[x-1][y-1] == int(input())
            confirmSmallWin(x-1,y-1,largeGrid[x-1][y-1])
            if largeGrid[x-1][y] == 0:
                for bigY in range (1,4):
                    for bigX in range (1,4):
                        print("Which player has tile x", bigX, " y", bigY, "?")
                        grid[bigX-1][bigY-1] = int(input())
    return