"""
Tres personas deciden invertir su dinero para fundar una empresa. 
Cada una de ellas invierte una cantidad distinta. 
Obtener el porcentaje que cada quien invierte con respecto 
a la cantidad total invertida.
"""
persona1 = input("Ingrese nombre: ")
monto1 = float(input(persona1 + " invertirá: "))
persona2 = input("Ingrese nombre: ")
monto2 = float(input(persona2 + " invertirá: "))
persona3 = input("Ingrese nombre: ")
monto3 = float(input(persona3 + " invertirá: "))
total = monto1 + monto2 + monto3

print(persona1, "invirtió", monto1 / total * 100, "%")
print(persona2, "invirtió", monto2 / total * 100, "%")
print(persona3, "invirtió", monto3 / total * 100, "%")