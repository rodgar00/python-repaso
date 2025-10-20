import random

class Carta:
    def __init__(self, valor, palo, nombre):
        self.valor = valor
        self.palo = palo
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} de {self.palo}"


valor = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 10,
    9: 10,   # Caballo
    10: 10   # Rey
}


def llenarBaraja():
    baraja = []
    palos = ["espadas", "oros", "copas", "bastos"]
    for palo in palos:
        for j in range(1, 11):
            if j == 1:
                carta = Carta(1, palo, "As")
            elif j < 8:
                carta = Carta(j, palo, str(j))
            else:
                figuras = ["Sota", "Caballo", "Rey"]
                carta = Carta(10, palo, figuras[j - 8])
            baraja.append(carta)
    return baraja


baraja = llenarBaraja()


def sacarCarta(baraja):
    indice = random.randint(0, len(baraja) - 1)
    return baraja.pop(indice)


def repartirCartas():
    carta_crupier = sacarCarta(baraja)
    carta_jugador = sacarCarta(baraja)

    valor_crupier = carta_crupier.valor
    valor_jugador = carta_jugador.valor

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
    nueva_carta = sacarCarta(baraja)
    valor_crupier += nueva_carta.valor
    print(f"Nueva carta crupier: {nueva_carta} (total: {valor_crupier})")
print()

salir = False
while valor_jugador < 21 and not salir:
    pedir = input("¿Quieres pedir una nueva carta? s/n -> ")
    if pedir.lower() == "s":
        print("El jugador pide otra carta...")
        nueva_carta = sacarCarta(baraja)
        print(f"Nueva carta jugador: {nueva_carta}")
        if nueva_carta.nombre == "As":
            if valor_jugador + 11 > 21:
                valor_jugador += 1
            else:
                valor_jugador += 11
        else:
            valor_jugador += nueva_carta.valor
        print(f"Total jugador: {valor_jugador}")
    elif pedir.lower() == "n":
        salir = True

print(f"\nPuntajes finales:")
print(f"Jugador: {valor_jugador}")
print(f"Crupier: {valor_crupier}\n")
comprobarGanador(valor_jugador, valor_crupier)
