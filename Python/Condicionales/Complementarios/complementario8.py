"""
Calcular el número de pulsaciones que una persona 
debe tener por cada 10 segundos de ejercicio, 
si la fórmula es: Número de pulsaciones = (220 - edad)/10
"""

edad = int(input("Ingrese su edad: "))
pulsaciones = (220 - edad) / 10
print("Usted debe tener %s pulsaciones por cada 10 segundos" % (pulsaciones))