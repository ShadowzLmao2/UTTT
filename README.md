# UTTT
Solving Ultimate Tic-Tac-Toe is the aim
The goal is to create opening theory and include the already solved endgame code to make the best AI assistant and opponent. 
The scope of the project includes:
- showing the amount of possible positions per turn and in total below 
- improving any program that solves the endgame by expanding the depth
- proving the best openings and temporarily good openings (until it is solved)
- ideally not using Monte Carlo code because I don't want to read it

Why this is coded in Python: this is my first Python project and wanted to learn how to code in Python

Notation: On the first turn or if the player can move anywhere, the xy coordinates of the bigger grid are written first (ex 1.2222 being middle-middle). After a move, a comma is written and then the second players move is written (ex. 1.2222,12). Different turns are represented by a space and then the turn number and a period (ex. 1.2222,12 2.22,33). Moves are assumed to be in the bigger grid where the last move was unless 4 digits are written.

Number of possible gamestates per move:
- Turn 1: 15 
- Turn 2: 103
- Turn 3: 821
- Turn 4: ?
