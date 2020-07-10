#Menu
#Operaciones
#S. Suma
#R. Resta
#M. Multiplicacion
#D. Division
#A. Salir
#Que opcion elige? :

#Ingrese numero uno
#Ingrese numero dos

print("Programa para resolver operaciones aritmeticas")
while True:
    print('''Operaciones: 1.- S. Suma 2.- R. Resta 3.- M. Multiplicacion 4.- D. Division 5.- A. Salir 
    ¿Que opcion elige? : ''')


    resp = input("Ingrese una opcion: ").upper()
    if resp == "S" or resp == "R" or resp == "M" or resp == "D":

        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))

        if resp == "S":
            print(f"La suma es: {num1 + num2}")

        elif resp == "R":
            print(f"La resta es: {num1 - num2}")

        elif resp == "M":
            print(f"La multiplicacion es: {num1 * num2}")
    
        elif resp == "D":
            print(f"La division es: {num1 / num2}")

    elif resp == "A":
            print("SALIR")
            break
