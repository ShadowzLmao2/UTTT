from convert_matrix import *
from functions import *
from main import *
from enum import Enum
from standardttt import standardGrid
class winState(Enum):
    draw = 0
    win  = 1
    loss = 2
    lose = 2

def isGameEndable(): #for UTTT
    if countEmptySpaces() == 1:
       fillLastSpace()
    drawGrid()

def solveFinalBoard(): #Solves the board when the only open spaces are in one board
    return

def singleTTTGameSolver(playerTurn):
    if smallEmptySpaces() <= 1 or smallEmptySpaces() == 9:
        return winState.draw
    if winInOne():
        return winState.win
    if loseInOne():
        return winState.lose
    return

def winInOne():
    return False

def loseInOne():
    return False

def countEmptySpaces():
    count = 0
    global grid
    for y in range(0,9):
        for x in range(0,9):
            if grid[x][y] == 0:
                count+=1
    return count

def smallEmptySpaces():
    count = 0
    global standardGrid
    for y in range(0,3):
        for x in range(0,3):
            if standardGrid[x][y] == 0:
                count+=1
    return count

def fillLastSpace():
    for y in range(0,9):
        for x in range(0,9):
            if grid[x][y] == 0:
                grid[x][y] = playerTurn

#Only possible moves on turn one is:
#11:11,21,31,22,33,
#12:11,21,21,22,13,23
#22:11,21,22