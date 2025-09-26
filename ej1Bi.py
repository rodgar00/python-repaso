"""
1. Dibujar una matriz cuadrada con el tamaño definido por el usuario y que pinte de 1 la diagonal inversa.

"""



from utilities import printMatriz

matriz = []

userInput = int(input("Introduce la cantidad de filas y columnas (matriz cuadrada) -> "))

for nFilas in range(userInput):
    matriz.append([])
    for nColumnas in range(userInput):
        if nFilas + nColumnas == userInput - 1:
            matriz[nFilas].append(1)
        else:
            matriz[nFilas].append(0)

#

printMatriz(matriz)