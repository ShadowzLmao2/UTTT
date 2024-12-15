from functions import *
from solve_game import *
def main():
    drawGrid()
    openMove()
    if simplify_board:
        simplifyBoard()
    while gameDone != True:
        takeMove()
main() 
