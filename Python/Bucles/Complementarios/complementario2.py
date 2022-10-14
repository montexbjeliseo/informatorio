# Desarrollar una solución que calcule la suma de los cuadrados 
# de los n primeros números naturales: 1 + 22 + 32 +… + n2.

indices = int(input("Ingrese cantidad de índices: "))
sumatoria = 0
for i in range(indices+1):
    sumatoria += i**2
    print(i**2)
print("Resultado: ", sumatoria)