from convert_matrix import *
from functions import *
from main import *

def isGameEndable():
    if countEmptySpaces() == 1:
       fillLastSpace()
    drawGrid()

def solveFinalBoard(): #Solves the board when the only open spaces are in one board
    return
def countEmptySpaces():
    count = 0
    global grid
    for y in range(0,9):
        for x in range(0,9):
            if grid[x][y] == 0:
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