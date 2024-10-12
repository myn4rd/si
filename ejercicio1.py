from functions1 import *
import numpy as np

class primer_ejercicio:
    def primer_sistema():
        print("Primer ejercicio")
        print("Primer sistema de ecuaciones")
        n = [[-8, +3, -7 ], [1, -2, -4], [-5, +1, -6]]
        nX = [[24, +3, -7], [-29, -2, -4], [7, 1, -6]]
        nY = [[-8, 24, -7], [1, -29,-4], [-5, 7, -6]]
        nZ = [[-8, 3, 24], [1, -2, -29], [-5, 1, 7]]

        Detn = Det3x3(n)

        variables = [nX, nY, nZ]

        determinantes_variables = []
        for i,matriz in enumerate(variables):
            determinante = Det3x3(matriz)
            determinantes_variables.append(determinante)
        valor_variables = []
        for i, variable in enumerate(determinantes_variables):
            resultado = variable / Detn 
            valor_variables.append(resultado)
        print(f"Resultado: {valor_variables}")

    def segundo_sistema(): 
        print("\nSegundo sistema de ecuaciones")
        n = [[-3, -2, +8 ], [2, 2, -9], [-6, -4, 10]]
        nX = [[-33, -2, +8], [51, 2, -9], [-12, -4, 10]]
        nY = [[-3, -33, +8], [2, 51, -9], [-6,-12, 10]]
        nZ = [[-3, -2, -33], [2, 2, 51], [-6, -4, -12]]

        Detn = Det3x3(n)

        variables = [nX, nY, nZ]

        determinantes_variables = []
        for i,matriz in enumerate(variables):
            determinante = Det3x3(matriz)
            determinantes_variables.append(determinante)
        valor_variables = []
        for i, variable in enumerate(determinantes_variables):
            resultado = variable / Detn 
            valor_variables.append(resultado)
        print(f"Resultado: {valor_variables}") 

    def tercer_sistema():
        print("\nTercer sistema de ecuaciones")
        n = [[7, -9, -6], [-1, 4, 3], [7, 6, -2]]
        nX = [[18, -9, -6], [-3, 4, 3], [47, 6, -2]]
        nY = [[7, 18, -6], [-1, -3, 3], [7, 47, -2]]
        nZ = [[7, -9, 18], [-1, 4, -3], [7, 6, 47]]


        Detn = Det3x3(n)

        variables = [nX, nY, nZ]

        determinantes_variables = []
        for i,matriz in enumerate(variables):
            determinante = Det3x3(matriz)
            determinantes_variables.append(determinante)
        valor_variables = []
        for i, variable in enumerate(determinantes_variables):
            resultado = variable / Detn
            valor_variables.append(resultado)
        print(f"Resultado: {valor_variables}")

class segundo_ejercicio:
    
    def nombre(Mat1, Mat2,abc):
        nombre = "KARIM LOPEZ GARCIA"
        nombreNum = len(nombre)
        Num = []
        for i in range(nombreNum):
            character = nombre[i]
            number = abc[character]
            Num.append(number)
        numRows = (nombreNum + 1) // 2
        numCols = 2
        matrixSize = numRows * numCols
        if len(Num) < matrixSize:
            Num.extend([0] * (matrixSize - len(Num)))
        M = np.array(Num).reshape(numRows, numCols)
        
        resultado1 = MatrixProduct(M, Mat1)
        resultado2 = MatrixProduct(M, Mat2)
        print("\nEjercicio 2")
        print("Método de cifrado 0")
        print(f"Nombre: {nombre}")
        print(f"Multiplicado por la matriz 1:{resultado1}")
        print(f"Multiplicado por la matriz 2:{resultado2}")
    
    def frase(Mat1,Mat2,abc):
        nombre = "TENGO SUEÑO Y HAMBRE"
        nombreNum = len(nombre)
        Num = []
        for i in range(nombreNum):
            character = nombre[i]
            number = abc[character]
            Num.append(number)
        numRows = (nombreNum + 1) // 2
        numCols = 2
        matrixSize = numRows * numCols
        if len(Num) < matrixSize:
            Num.extend([0] * (matrixSize - len(Num)))
        M = np.array(Num).reshape(numRows, numCols)
        
        resultado1 = MatrixProduct(M, Mat1)
        resultado2 = MatrixProduct(M, Mat2)
        print("\nMétodo de cifrado 0")
        print(f"Frase: {nombre}")
        print(f"Multiplicado por la matriz 1:{resultado1}")
        print(f"Multiplicado por la matriz 2:{resultado2}")
    
    def frases(Mat1,Mat2,abc):
       # frases = ["JOJOJOJOJO", "LOLOLOLOLOL", "XDXDXDXDXDX"]
        for i in frases:
            nombre = i
            nombreNum = len(nombre)
            Num = []
            for i in range(nombreNum):
                character = nombre[i]
                number = abc[character]
                Num.append(number)
            numRows = (nombreNum + 1) // 2
            numCols = 2
            matrixSize = numRows * numCols
            if len(Num) < matrixSize:
                Num.extend([0] * (matrixSize - len(Num)))
            M = np.array(Num).reshape(numRows, numCols)

            resultado1 = MatrixProduct(M, Mat1)
            resultado2 = MatrixProduct(M, Mat2)
            print("\nMétodo de cifrado 0")
            print(f"Frase: {nombre}")
            print(f"Multiplicado por la matriz 1:{resultado1}")
            print(f"Multiplicado por la matriz 2:{resultado2}")

class tercer_ejercicio: 
    def frases1(Mat3,Mat4,abc): 
        for i in frases:
            nombre = i
            nombreNum = len(nombre)
            Num = []
            for i in range(nombreNum):
                character = nombre[i]
                number = abc[character]
                Num.append(number)
            numRows = (nombreNum + 1) // 2
            numCols = 3
            matrixSize = numRows * numCols
            if len(Num) < matrixSize:
                Num.extend([0] * (matrixSize - len(Num)))
            M = np.array(Num).reshape(numRows, numCols)

            resultado1 = MatrixProduct(M, Mat3)
            resultado2 = MatrixProduct(M, Mat4)
            print("\nMétodo de cifrado 0")
            print(f"Frase: {nombre}")
            print(f"Multiplicado por la matriz 1:{resultado1}")
            print(f"Multiplicado por la matriz 2:{resultado2}")

class quinto_ejercicio:
    def cifrado_1(E1, E2, E3, abc):
        for i in frases:
            frase = i
            fraseNum = len(frase)
            Num = []
            for i in range(fraseNum): 
                character = frase[i]
                number = abc[character]
                Num.append(number)
            print(Num)





ejercicios = ["primer_sistema", "segundo_sistema", "tercer_sistema"]

for i, ejercicio in enumerate(ejercicios):
    metodo = getattr(primer_ejercicio, ejercicio)
    metodo()


frases = ["JOJOJOJOJO", "LOLOLOLOLOL", "XDXDXDXDXDX"]
Mat1 = [[ 5, -6 ], [2, 3]] 
Mat2 = [[ 2, -1 ], [14, -7]]
key = {' ' : 0, 'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 
         'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 
         'N' : 14, 'Ñ' : 15, 'O' : 16, 'P' : 17, 'Q' : 18, 'R' : 19, 'S' : 20,
          'T' : 21, 'U' : 22, 'V' : 23, 'W' : 24, 'X' : 25, 'Y' : 26, 'Z' : 27}
 
ejercicios2 = ["nombre","frase","frases"]

for i, ejercicio2 in enumerate(ejercicios2):
    metodo2 = getattr(segundo_ejercicio, ejercicio2)
    metodo2(Mat1,Mat2,key)

Mat3 = [[1,2,-1], [2,-1,3], [3,1,2]]
Mat4 = [[8,4,3], [-5,6, -2], [7,9,-8]]

print("\nEjercicio 3")
tercer_ejercicio.frases1(Mat3,Mat4,key)

E1=[[1,4,6], [3,5,9], [2,7,8]] 
E2=[[-6,8,-2], [-9,-6,-7], [-7, -6,-1]]
E3=[[4,-3,1], [-5,2,0], [8,-6,2]]


print("\nEjercicio 5")
quinto_ejercicio.cifrado_1(E1,E2,E3,key)
