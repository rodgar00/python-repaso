"""
3. Comprobar si una matriz dada es un cuadrado mágico (suma filas columnas y diagonales suman lo mismo)
cuadradoMágico = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
"""

matriz = [[16,3,2,13],
          [5,10,11,8],
          [9,6,7,12],
          [4,15,14,1]]

diagonalPP = []
for i in range(4):
    sumaPP = 0
    sumaPP += matriz[i][i]
    diagonalPP.append(sumaPP)

diagonalSec = []
for i in range(4):
    sumaSec = 0
    sumaSec += matriz[i][4 - 1 - i]
    diagonalSec.append(sumaSec)

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




if diagonalPP and diagonalSec and resultadoC and resultadoF:
    print("Es mágico")
else:
    print("No es mágico")