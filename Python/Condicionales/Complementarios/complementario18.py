"""
Se leen tres números que son las longitudes de los lados 
de un triángulo. 
Determinar e informar si el mismo es equilátero (3 lados iguales), 
isósceles (2 lados iguales) o escaleno (3 lados distintos).
"""

l1 = float(input("Ingrese longitud: "))
l2 = float(input("Ingrese longitud: "))
l3 = float(input("Ingrese longitud: "))

if l1 == l2 == l3:
    tipo = "equilátero"
elif l1 == l2 or l1 == l3 or l2 == l3:
    tipo = "isósceles"
else :
    tipo = "escaleno"

print("Es un triángulo", tipo)