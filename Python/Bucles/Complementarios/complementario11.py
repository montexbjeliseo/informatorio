# Hacer un programa que permita determinar todos los divisores
# de un número ingresado por el teclado.
num = int(input("Ingrese un valor: "))
for i in range(1, num+1):
    if num % i == 0:
        print(i)