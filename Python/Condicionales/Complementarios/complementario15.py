"""
Un obrero necesita calcular su salario semanal, 
el cual se obtiene de la siguiente manera:

i. Si trabaja 40 horas o menos se le paga $16 por hora

ii. Si trabaja más de 40 horas se le paga $16 por cada 
una de las primeras 40 horas y $20 por cada hora extra."""

horas = int(input("Horas trabajadas: "))
extras = 0

if horas > 40:
    extras=horas - 40
print("Su salario semanal es de:", horas*16+extras*20)