"""
 Un grupo de 100 estudiantes presentan un exámen de Física. 
 Diseñe un diagrama que lea por cada estudiante la calificación 
 obtenida y calcule e imprima:

A.- La cantidad de estudiantes que obtuvieron 
    una calificación menor a 50.

B.- La cantidad de estudiantes que obtuvieron 
    una calificación de 50 o más pero menor que 80.

C.- La cantidad de estudiantes que obtuvieron 
    una calificación de 70 o más pero menor que 80.

D. La cantidad de estudiantes que obtuvieron 
    una calificación de 80 o más."""

a = 0
b = 0
c = 0
d = 0
cantidad = 100
for i in range(cantidad):
    calificacion = float(input("Ingrese calificación: "))
    if calificacion >= 80:
        d += 1
    elif calificacion >=70:
        c += 1
    elif calificacion >= 50:
        b += 1
    else :
        a += 1
print("Alumnos con calificación de menos de 50:", a)
print("- Porcentaje:", a / cantidad * 100)
print("Alumnos con calificaciónde 50 o más:", b)
print("- Porcentaje:", b / cantidad * 100)
print("Alumnos con calificación de 70 o más:", c)
print("- Porcentaje:", c / cantidad * 100)
print("Alumnos con calificación de 80 o más:", d)
print("- Porcentaje:", d / cantidad * 100)