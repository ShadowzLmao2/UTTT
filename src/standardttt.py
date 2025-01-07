from config import *
standardGrid = (
    ([0]*3),
    ([0]*3),
    ([0]*3))

def drawStandard():
    for y in range(0,3):
        for x in range(0,3):
            if standardGrid[x][y] == 0:
                print("-", end="")
            elif standardGrid[x][y] == 1 and not x_and_o_numbers:
                print("X", end="")
            elif standardGrid[x][y] == 2 and not x_and_o_numbers:
                print("O", end="")
            elif standardGrid[x][y] == 2 and x_and_o_numbers:
                print("X", end="")
            else:
                print("O", end="")
            if x == 2:
                print("")
            else:
                print("|", end="")
drawStandard()