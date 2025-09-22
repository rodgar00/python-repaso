# for i in range(1,10,2): saltos de 2 en 2 hasta llegar a 10 desde 1

#Calculadora con bucle
#Suma,resta,mul,div
#Salga si el usuario pide salir

userInput = int(input("Introduce la operación \n1. suma\n2. resta\n3. multiplicación\n4. división\n"))


continuar = True
while continuar and userInput <= 4:
    if userInput == 1:
        userInputOp1 = int(input("Introduce el primer número-> "))
        userInputOp2 = int(input("Introduce el segundo número-> "))
        print(userInputOp1+userInputOp2)
        continuar = False
    if userInput == 2:
        userInputOp1 = int(input("Introduce el primer número-> "))
        userInputOp2 = int(input("Introduce el segundo número-> "))
        print(userInputOp1-userInputOp2)
        continuar = False
    if userInput == 3:
        userInputOp1 = int(input("Introduce el primer número-> "))
        userInputOp2 = int(input("Introduce el segundo número-> "))
        print(userInputOp1*userInputOp2)
        continuar = False
    if userInput == 4:
        userInputOp1 = int(input("Introduce el primer número-> "))
        userInputOp2 = int(input("Introduce el segundo número-> "))
        print(userInputOp1/userInputOp2)
        continuar = False
else:
    continuar = False