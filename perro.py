class Perro:
    raza = "Chihuahua"
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def __str__(self):
        return f"Soy {self.nombre}, tengo {self.edad} años y mi raza es {self.raza}."

    def comer(self, comidaEnGramos):
        self.peso += comidaEnGramos
        print(f"{self.nombre} comió {comidaEnGramos} gramos, y ahora pesa {self.peso}")

    def cagar(self, cacaEnGramos):
        self.peso -= cacaEnGramos
        print(f"{self.nombre} expulsó {cacaEnGramos} gramos, y ahora pesa {self.peso}")




