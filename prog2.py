#Escribir un programa que pida al usuario 2 numeros enteros y calcular la suma
#desde el numero 1 hasta el numero 2
#Imprimir resultado de la suma
print("Ejercicio")
num1= int(input("Ingresa el primer numero"))
num2= int(input("Ingrese el segundo numero"))

total=0

for num in range (num1,num2+1):
    total += num

print("El resultado es: ",total)