from functions import *
def main():
    drawGrid()
    while gameDone != True:
        if freeMove:
            openMove()
        else:
            takeMove()
main() 
