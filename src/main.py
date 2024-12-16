from functions import *
from solve_game import *
from import_game import *
from config.general import *
def main():
    if ask_to_import:
        shouldImport()
    else:
        drawGrid()
        openMove()
    while gameDone != True:
        takeMove()

def shouldImport():
    print("Would you like to import a game? (y/n): ", end="")
    yesOrNoInput = input()
    if yesOrNoInput == "y":
        askForBoardState()
        drawGrid()
    else:
        drawGrid()
        openMove()
    return

main() 