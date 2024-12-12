# UTTT
Solving Ultimate Tic-Tac-Toe for the first time in forever
The goal is to create opening and include the already solved endgame code to make the best AI assistant and opponent. 
The scope of the project includes:
    showing the amount of possible positions below 
    showing the total number of games possible
    showing the best openings and temporarily good openings (until it is solved)
    hopefully not using Monte Carlo code because I don't want to read

Number of possible gamestates per move
    Every odd move is player 1 and every even move is player 2.
    Games are denoted using a grid system where coordinates in the big grid are denoted first. For example, 1.2222 is player 1 playing the very middle on their first turn. 2.2211 is the second player playing in the top left of the middle tile. Commas can be used as such: 3.11,33 where this is the first player's second move in the bottom left of the top right tile
    Turn 1: 15
        Ideal Move: Middle-Middle (2222)
    Turn 2: ?
