A = [[1, 1, 1, 5],
    [2, 7, 0, 500],
    [2, 0, 300, 700]]

# assuming n by n+1 matrix
def solveMatrix(matrix, size):
    for i in range(size):
        # preprocess the matrix
        currentPivot = abs(matrix[i][i])
        maxRow = i
        row = i + 1
        while row < size:
            if abs(matrix[row][i]) > currentPivot:
                currentPivot = abs(matrix[row][i])
                maxRow = row
            row += 1
        matrix = swapRows(matrix, i, maxRow, size)

        matrix = setPivotToOne(matrix, i, i, size)
        row = i + 1
        while row < size:
            matrix = nullify(matrix, row, i, size, matrix[i][i])
            row += 1
    for i in range(1, size):
        row = i - 1
        while row >= 0:
            matrix = nullify(matrix, row, i, size, matrix[i][i])
            row -= 1

    return matrix

def identityMatrix(size):
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(0)

    for i in range(size):
        matrix[i][i] = 1
    return matrix

def swapRows(matrix, row1, row2, size):
    identity = identityMatrix(size)
    identity[row1], identity[row2] = identity[row2], identity[row1]
    return multiplyMatrices(identity, matrix, size)

def editMatrix(matrix, x, y, val):
    matrix[x][y] = val
    return matrix

# assuming nxn+1 matrix
def multiplyMatrices(matrix1, matrix2, size):
    mat = []
    for i in range(size+1):
        mat.append([])

    for i in range(size):
        for j in range(size + 1):
            sum = 0
            for k in range(size):
                sum += matrix1[i][k] * matrix2[k][j]
            mat[i].append(sum)

    printMultiplication(matrix1, matrix2, mat, size, size)
    return mat

def nullify(matrix, x, y, size, pivot):
    identity = identityMatrix(size)
    return multiplyMatrices(editMatrix(identity, x, y, -1*matrix[x][y]/pivot), matrix, size)

def setPivotToOne(matrix, x, y, size):
    identity = identityMatrix(size)
    return multiplyMatrices(editMatrix(identity, x, y, 1/matrix[x][y]), matrix, size)

def printMatrix(A, size, size2):
    for i in range(size):
        for j in range(size2):
            print(A[i][j], end=' ')
        print()

# assuming nxn+1
def printMultiplication(A, B, res, size, size2):
    for i in range(size):
        print('[', end =' ')
        for j in range(size2):
            print('{:6.2f}'.format(A[i][j]), end='\t')
        print('] [', end =' ')
        for j in range(size2 + 1):
            print('{:6.2f}'.format(B[i][j]), end='\t')
        print(']\t\t[', end=' ')
        for j in range(size2 + 1):
            print('{:6.2f}'.format(res[i][j]), end='\t')
        print(']', end='')
        print()
    print()

printMatrix(solveMatrix(A, 3), 3, 4)