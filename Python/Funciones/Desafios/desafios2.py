"""
Realiza una función llamada relacion(a, b) que a partir de toneladas 
recicladas de dos ciudades se cumpla lo siguiente:

    Si el primer número es mayor que el segundo, 
    debe devolver el nombre de la ciudad 1.

    Si el primer número es menor que el segundo, 
    debe devolver el nombre de la ciudad 2.

    Si ambos números son iguales, 
    debe devolver el nombre de ambas.
"""

def relacion(a, b):
    if a > b:
        return ciudadA
    elif a < b:
        return ciudadB
    else :
        return ciudadA + ", " + ciudadB
vivo = True
while(vivo):
    ciudadA = input("Ingrese el nombre de la primer ciudad: ")
    ciudadB = input("Ingrese el nombre de la segunda ciudad: ")
    tonsA = int(input("Ingrese cantidad de toneladas A: "))
    tonsB = int(input("Ingrese cantidad de toneladas b: "))
    print(relacion(tonsA, tonsB))
    q = input("Continuar? (s - para sí): ").lower()
    if q != "s":
        vivo = False
