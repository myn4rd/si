# Dada una matriz M de 2x2, calcula el determinante
def Det2x2(M):
    result = M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return result

# Dada una matriz M de 3x3, calcula el determinante
# Dada una matriz M de 3x3, calcula el determinante
def Det3x3(M):
    result = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) -
              M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) +
              M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    return result


# Dada una matriz A y un vector u, calcula su prodcut

def MatrixVectorProduct(A, u):
    numFil = len(A)
    numCol = len(A[0])
    v = [0] * numFil
    for i in range(numFil):
        vi = 0
        for j in range(numCol):
            vi += A[i][j]*u[j]
        v[i] = vi
    return v


# Dadas dos matrices cuadradas de tamaño arbitrario, calcula el producto
# de las matrices
def MatrixProduct(A, B):
    filA = len(A)
    colA = len(A[0])
    filB = len(B)
    colB = len(B[0])
    
    # Comprobación de compatibilidad de dimensiones
    if colA != filB:
        raise ValueError("Las matrices no se pueden multiplicar: número de columnas de A debe ser igual al número de filas de B.")
    
    # Inicializa la matriz producto
    C = [[0] * colB for j in range(filA)]
    for i in range(filA):
        for j in range(colB):
            cij = 0
            for k in range(colA):
                cij += A[i][k] * B[k][j]
            C[i][j] = cij
    return C


# Dada una matriz M y los índices de fila y columna
# Crea una nueva matriz eliminando la fila y columna dadas 
def ReducedMatrix(M, fil, col):
    redMat = []
    for i in range(3):
        if i != fil:
            newFil = []
            for j in range(3):
                if j != col:
                    newFil.append(M[i][j])
            redMat.append(newFil)
    return redMat

# Dada una matriz M, calcula la matriz de cofactores
def CofactorMatrix(M):
    result = [[0]*3 for j in range(3)]
    for i in range(3):
        for j in range(3):
            redMat_ij = ReducedMatrix(M, i, j)
            result[i][j] = (-1)**(i+j) * Det2x2(redMat_ij)

    return result

# Dado un vector, crea un vector con componentes mod n
def TakeModulus(vector, n):
    numComp = len(vector)
    result = [0] * numComp
    for i in range(numComp):
        result[i] = vector[i] % n
    return result
