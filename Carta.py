class Carta:
    def __init__(self, valor, palo, nombre):
        self.valor = valor
        self.palo = palo
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} de {self.palo}"