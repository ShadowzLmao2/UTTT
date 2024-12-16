from functions import *
inputtedPlayer = 0
def askForBoardState():
    global largeGrid
    global grid
    #takes from 9 to 81 inputs to complete, need a better solution
    for y in range (1,4):
        for x in range (1,4):
            print("Which player won x", x, "and y", y, "?")
            inputtedPlayer == int(input())
            largeGrid[x-1][y-1] = inputtedPlayer
            if inputtedPlayer != 0:
                for miniY in range(0,3):
                    for miniX in range(0,3):
                        grid[miniY+(y*3-3)][miniX+(x*3-3)] = inputtedPlayer
            #else:
                for bigY in range (1,4):
                    for bigX in range (1,4):
                        print("Which player has tile x", bigX, " y", bigY, "?")
                        grid[bigX-1][bigY-1] = int(input())
    print("Whose turn is it? (X=1, O=2)")
    global playerTurn
    playerTurn = int(input())
    return