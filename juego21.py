import random

from Carta import Carta

cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valor = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 10,
    9: 10,
    10: 10
}


"""def llenarBaraja():
    baraja = []
    palos = ["espadas", "oros", "copas", "bastos"]
    for i in range(4):
        for j in range(1, 11):
            if j == 1:
                carta = Carta(1, palos[i], "As")
            elif j < 8:
                carta = Carta(j, palos[i], j)
            else:
                figuras = ["Sota", "Caballo", "Rey"]
                carta = Carta(10, palos[i], figuras[j-8])
            baraja.append(carta)
    return baraja

baraja = llenarBaraja()
for carta in baraja:
    print(carta)
    print(f"El valor de la carta es {carta.valor}")
"""
def repartirCartas():
    carta_crupier = random.choice(cartas)
    carta_jugador = random.choice(cartas)

    valor_crupier = valor.get(carta_crupier)
    valor_jugador = valor.get(carta_jugador)

    print(f"Carta crupier: {carta_crupier} (valor: {valor_crupier})")
    print(f"Carta jugador: {carta_jugador} (valor: {valor_jugador})")

    return valor_crupier, valor_jugador


def comprobarGanador(valor_jugador, valor_crupier):
    if valor_jugador > 21:
        print("Te has pasado, gana la casa.")
    elif valor_crupier > 21:
        print("La casa se ha pasado, ganas tú.")
    elif valor_jugador > valor_crupier:
        print("Ganas tú")
    elif valor_crupier > valor_jugador:
        print("Gana la casa.")
    else:
        print("Empate.")

valor_crupier, valor_jugador = repartirCartas()

while valor_crupier < 16:
    print("El crupier pide otra carta...")
    nueva_carta = random.choice(cartas)
    valor_crupier += valor.get(nueva_carta)
    print(f"Nueva carta crupier: {nueva_carta} (total: {valor_crupier})")
print()

salir = False
while valor_jugador < 21 and salir == False:
    pedir = input("¿Quieres pedir una nueva carta? s/n -> ")
    if pedir == "s":
        print("El jugador pide otra carta...")
        nueva_carta = random.choice(cartas)
        valor_jugador += valor.get(nueva_carta)
        print(f"Nueva carta jugador: {nueva_carta} (total: {valor_jugador})")
        if nueva_carta is 1 and 11+valor_jugador > 21:
            valor
    elif pedir == "n":
        salir = True

print(f"{valor_jugador} jugador, {valor_crupier} crupier")
comprobarGanador(valor_jugador, valor_crupier)


