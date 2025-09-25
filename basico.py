"""
Pasar de minutos a horas y resto (mins)
"""

minutos = int(input("Introduce los minutos -> "))

horas = minutos // 60
resto = minutos % 60

if resto == 0:
    print(f"Hay {horas} horas")
else:
    print(f"Hay {horas} horas y {resto} minutos")
