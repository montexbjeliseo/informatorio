"""
Diseñar un programa que lea las longitudes de los tres lados 
de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es, 
de acuerdo a los siguientes casos. 
Suponiendo que A determina el mayor de los tres lados 
y B y C corresponden con los otros dos, entonces:

Si A>=B + C à No se trata de un triángulo

Si A2 = B2 + C2 à Es un triángulo rectángulo

Si A2 > B2 + C2 à Es un triángulo obtusángulo

Si A2 < B2 + C2 à Es un triángulo acutángulo
"""

l1 = int(input("Ingrese longitud: "))
l2 = int(input("Ingrese longitud: "))
l3 = int(input("Ingrese longitud: "))

a = max(l1, l2, l3)

bc = 0
bc = bc if a == l1 else bc + l1
bc = bc if a == l2 else bc + l3
bc = bc if a == l3 else bc + l2

if a >= bc:
    print("No se trata de un triangulo")
elif a == bc:
    print("Es un triángulo rectángulo")
elif a > bc:
    print("Es un triángulo obtusángulo")
elif a < bc:
    print("Es un triángulo acutángulo")