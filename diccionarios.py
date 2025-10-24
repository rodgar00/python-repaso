def comprobar_errores(texto):
    if not texto:
        print("No puede estar vacío.")
        return None
    if texto.isnumeric():
        print("No puede ser solo un número.")
        return None
    return True


def comprobar_vacio(texto):
    if not texto:
        print("No puede estar vacío.")
        return None
    return True


def pedir_tipo_dato():
    tipo_valido = False
    tipo = ""
    while not tipo_valido:
        tipo = input("Elige el tipo de valor (str, int, float): ").lower()
        if comprobar_errores(tipo):
            if tipo in ("str", "int", "float"):
                tipo_valido = True
            else:
                print("Tipo no válido. Usa 'str', 'int' o 'float'.")
    return tipo


def pedir_clave():
    clave_valida = False
    clave = ""
    while not clave_valida:
        clave = input("Introduce la clave: ")
        clave_valida = comprobar_errores(clave)
    return clave


def pedir_valor():
    valor_valido = False
    valor = ""
    while not valor_valido:
        valor = input("Introduce el valor: ")
        valor_valido = comprobar_vacio(valor)
    return valor


diccionario = {}


seguir = True
while seguir:
    tipo = pedir_tipo_dato()
    clave = pedir_clave()
    valor = pedir_valor()

    conversion_exitosa = True

    if tipo == "str":
        diccionario[clave] = valor
    elif tipo == "int":
        try:
            diccionario[clave] = int(valor)
        except ValueError:
            print("Error: el valor no corresponde al tipo int.")
            conversion_exitosa = False
    elif tipo == "float":
        try:
            diccionario[clave] = float(valor)
        except ValueError:
            print("Error: el valor no corresponde al tipo float.")
            conversion_exitosa = False

    if conversion_exitosa:
        respuesta_valida = False
        while not respuesta_valida:
            respuesta = input("¿Quieres añadir otro valor? (s/n) -> ").lower()
            if respuesta == "s":
                respuesta_valida = True
                seguir = True
            elif respuesta == "n":
                respuesta_valida = True
                seguir = False
            else:
                print("Respuesta no válida. Introduce 's' o 'n'.")

print("\nDiccionario final")
for k, v in diccionario.items():
    print(f"{k}: {v}")
