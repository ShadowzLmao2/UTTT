from functions import *
def setUpGame():
    drawGrid()
    firstMove()
def main():
    setUpGame()
    while gameDone != True:
        takeMove()
        #checkSmallWin()
main()
