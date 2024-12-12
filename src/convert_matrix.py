def rotateCWMatrix(matrix):
    for i in range(0,9):
        for j in range(0,9):
            retMatrix[i][j] = matrix[8-j][i]
    return retMatrix

def rotateCCWMatrix(matrix):
    for i in range(0,9):
        for j in range(0,9):
            retMatrix[i][j] = matrix[j][8 - i]
    return retMatrix

def flipUpMatrix(matrix):
    for i in range(0,9):
        for j in range(0,9):
            retMatrix[i][j] = matrix[8-i][j]
    return retMatrix

def flipRightMatrix(matrix):
    for i in range(0,9):
        for j in range(0,9):
            retMatrix[i][j] = matrix[i][8-j]
    return retMatrix

retMatrix = (
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9),
    ([0]*9))