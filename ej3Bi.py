"""
3. Comprobar si una matriz dada es un cuadrado mágico (suma filas columnas y diagonales suman lo mismo)
cuadradoMágico = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
"""
matriz = [[16,3,2,13],
          [5,10,11,8],
          [9,6,7,12],
          [4,15,14,1]]

sumaPP = 0
for i in range(4):
    sumaPP += matriz[i][i]

sumaSec = 0
for i in range(4):
    sumaSec += matriz[i][len(matriz) - 1 - i]

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

es_magico = True

for f in resultadoF:
    if f != sumaPP:
        es_magico = False

for c in resultadoC:
    if c != sumaPP:
        es_magico = False

if sumaSec != sumaPP:
    es_magico = False

if es_magico:
    print("Es mágico")
else:
    print("No es mágico")
