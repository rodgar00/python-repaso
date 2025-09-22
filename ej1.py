import random

lista = []

for i in range(5):
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
