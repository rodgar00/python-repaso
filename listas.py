from perro import Perro

perrito = Perro("Tomasito", 4, 5000)
perron = Perro("Metallica", 7, 15000)
print(perrito)
print(perron)
print(perrito.nombre)
print(perrito.edad)
print(perrito.raza)

perrito.comer(200)
perrito.cagar(300)

perrito.peso = 2000 