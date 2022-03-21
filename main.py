A = [[55, 4, 5, 4],
    [-5, 8, 9, 5],
    [-6, 7, 11, 7]]

# assuming n by n+1 matrix
def solveMatrix(matrix, size):
    for i in range(size):
        matrix = setPivotToOne(matrix, i, i, size)
        row = i + 1
        while row < size:
            matrix = nullify(matrix, row, i, size, matrix[i][i])
            row += 1
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


def editMatrix(matrix, x, y, val):
    matrix[x][y] = val
    return matrix


def nullify(matrix, x, y, size, pivot):
    identity = identityMatrix(size)
    return multiplyMatrices(editMatrix(identity, x, y, -1*matrix[x][y]/pivot), matrix, size)


def setPivotToOne(matrix, x, y, size):
    identity = identityMatrix(size)
    return multiplyMatrices(editMatrix(identity, x, y, 1/matrix[x][y]), matrix, size)


# assuming n by n+1 matrix
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
    return mat


def printMatrix(A, size):
    for i in range(size):
        for j in range(size + 1):
            print(A[i][j], end=' ')
        print()


printMatrix(solveMatrix(A, 3), 3)