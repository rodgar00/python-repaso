"""
2. Llenar una matriz cuadrada (4x4) de números aleatorios del 0 al 9 y mostrar la suma de filas y columnas
"""
import random

from utilities import printMatriz

matriz = []

for nFilas in range(4):
    matriz.append([])
    for nColumnas in range(4):
        matriz[nFilas].append(random.randint(0,9))

resultadoF = []
for i in range(4):
    sumaF = 0
    for j in range(4):
        sumaF += matriz[i][j]
    resultadoF.append(sumaF)

resultadoC = []
for i in range(4):
    sumaC = 0
    for j in range(4):
        sumaC += matriz[j][i]
    resultadoC.append(sumaC)

printMatriz(matriz)

print("\nSuma de cada fila:")
for i, suma in enumerate(resultadoF):
    print(f"Fila {i + 1}: {suma}")

print("\nSuma de cada columna:")
for i, suma in enumerate(resultadoC):
    print(f"Columna {i + 1}: {suma}")

