# Determinar el número mayor de 10 números ingresados.
list = []
for i in range(10):
    list.append(int(input("Ingrese numero "+str(i+1)+"°: ")))
#mayor = max(list)
mayor = list[0]
for n in list:
    mayor = max(mayor, n)
print("El numero mayor de la lista es:", mayor)