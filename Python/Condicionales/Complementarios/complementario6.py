"""
Un equipo de fútbol ha tenido una buena campaña y 
desea premiar a sus jugadores con un aumento del salario 
para la siguiente campaña. 
Los sueldos deben ajustarse de la siguiente forma:

Sueldo Actual (en $)    Aumento
0 – 6000					   15%

6000 – 7900					   10%

7900 – 12000					6%

Más de 12000				    0%

Diseñar un programa que lea el salario de un jugador, 
y que a continuación muestre el tanto por ciento de aumento, 
el sueldo actual y el sueldo aumentado.
"""

salario = float(input("Ingrese monto del salario: "))
aumento = 0

if 0 <= salario < 6000:
    aumento = 15
elif 6000 <= salario < 7900:
    aumento = 10
elif 7900 <= salario < 12000:
    aumento = 6

print("Salario actual:", salario)
print("Salario con aumento: %s" % (salario + salario * aumento / 100))
print("Porcentaje de aumento:", str(aumento) + "%")