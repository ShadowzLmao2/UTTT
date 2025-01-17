from convert_matrix import *
from functions import *
from main import *
from enum import Enum
from standardttt import *
class winState(Enum):
    draw = 0
    win  = 1
    loss = 2
    lose = 2
    likelyDraw = 3
    unknown = 4 #temporary

def isGameEndable(): 
    if countEmptySpaces() == 1:
        fillLastSpace()
        drawGrid()
    return

def solveFinalBoard(): #Solves the board when the only open spaces are in one board
    return

def singleTTTGameSolver(turn):
    if countBlankSpaces() <= 1 or countBlankSpaces() == 9:
        return winState.draw
    if winInOne():
        return winState.win
    if loseInOne():
        return winState.lose
    return winState.unknown

def winInOne():
    return False

def loseInOne():
    return False

def fillLastSpace():
    for y in range(0,9):
        for x in range(0,9):
            if grid[x][y] == 0:
                grid[x][y] = turn

def solveSTTT():
    emptySpaces = countBlankSpaces()
    if emptySpaces == 0 or emptySpaces == 1:
        return winState.likelyDraw
    elif emptySpaces == 8:
        isGameWinnable()
    else:
        return winState.draw
    return winState.likelyDraw
#Only possible moves on turn one is:
#11:11,21,31,22,33,
#12:11,21,21,22,13,23
#22:11,21,22