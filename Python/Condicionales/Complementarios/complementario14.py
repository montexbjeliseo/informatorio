"""
Leer 2 números; si son iguales que los multiplique, si el primero 
es mayor que el segundo que los reste y si no que los sume.
"""

num1 = int(input("Ingrese valor: "))
num2 = int(input("Ingrese valor: "))

if num1 == num2:
    print("Multiplicar:", num1 * num2)
elif num1 > num2:
    print("Restar:", num1 - num2)
else:
    print("Sumar:", num1 + num2)