# UTTT
Solving Ultimate Tic-Tac-Toe is the aim
The goal is to create opening theory and include the already solved endgame code to make the best AI assistant and opponent. 
The scope of the project includes:
- showing the amount of possible positions below 
- improving any program that solves the endgame by expanding the depth
- showing the best openings and temporarily good openings (until it is solved)
- hopefully not using Monte Carlo code because I don't want to read

Why this is coded in Python: this is my first Python project and wanted to learn how to code in Python

Number of possible gamestates per move:
- Every odd move is player 1 and every even move is player 2.
- Notation uses the xy coordinates of the large grid and then the small grid. Player turns are separated by commas. For example, middle-middle and middle-topleft is denoted as 2222,2211
    - Turn 1: 15
        Ideal Move: Middle-Middle (2222), second best is Middle-Corner (2211)
    - Turn 2: 103 (moves for player two)
        Ideal Move: after 2222, 2211 is ideal according to AI, I can not explain why
    - Turn 3: ?
