#Determinar si el primero de un conjunto de tres números dados, 
#es menor que los otros dos

num1 = float(input("Ingrese un valor: "))
num2 = float(input("Ingrese un valor: "))
num3 = float(input("Ingrese un valor: "))

if num2 > num1 < num3:
    print("El primero numero es menor que los demás")
else: 
    print("El primero numero NO es menor que los demás")