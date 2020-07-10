#Escribir un porgrama que pida al usuario un texto y un numero entero
#Mandar a imprimir en pantalla el texto repetido las veces indicado por el numero.
#Nota importante: Hacer el programa usando una funcion
#Ingresa un texto: Hola
#Ingresa un numero: 4
#Salida:
#Hola
#Hola
#Hola
#Hola

#Declarar la funcion

def repetir(texto,numero):
    texto += "\n"
    print(texto*numero)

#Escribir el codigo para usar la funcion

t = input("Ingresa un texto: ")
n = int(input("Ingresa un numero: "))

repetir(t,n)
