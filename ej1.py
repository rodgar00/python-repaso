"""
Introducir nombres (min 5) y que se guarden en una lista para luego tener que adivinar el nombre
3 intentos
"""

import random

lista = []

cantidad = int(input("Introduce cuantos nombres quieres meter (mínimo 5) -> "))

while cantidad < 5:
    print("Introduce al menos 5")
    cantidad = int(input("Introduce cuantos nombres quieres meter (mínimo 5) -> "))

for i in range(cantidad):
    nombre = input(f"Introduce el nombre {i + 1}º: ")
    lista.append(nombre)

indiceAleatorio = random.randint(0, len(lista) - 1)
nombreRandom = lista[indiceAleatorio]

intentos = 3
adivinado = False

while intentos > 0 and not adivinado:
    nombreAdivinar = input("Pon el nombre que crees -> ")
    if nombreAdivinar == nombreRandom:
        print("Has adivinado")
        adivinado = True
    else:
        intentos -= 1
        if intentos > 0:
            print(f"No es correcto. Te quedan {intentos} intentos.")
        else:
            print(f"Has fallado. El nombre era: {nombreRandom}")
