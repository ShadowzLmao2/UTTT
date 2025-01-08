from functions import *
from import_game import *
from config import *
from convert_matrix import *

def main():
    if ask_to_import:
        shouldImport()
    else:
        drawGrid()
        openMove()
    while gameDone == False:
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
