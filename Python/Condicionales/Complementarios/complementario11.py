"""
Determinar si un alumno aprueba a reprueba un curso, 
sabiendo que aprobara si su promedio de tres calificaciones 
es mayor o igual a 70; desaprueba en caso contrario.
"""

nota1 = float(input("Ingrese calificación: "))
nota2 = float(input("Ingrese calificación: "))
nota3 = float(input("Ingrese calificación: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 70:
    print("El alumno aprobó con:", promedio)
else:
    print("El alumno NO aprobó con:", promedio)