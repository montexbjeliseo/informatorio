#Diseñar un programa que permita obtener el producto entre 
# A y B mediante sumas sucesivas.
multiplicando = int(input("Ingrese multiplicando: "))
multiplicador = int(input("Ingrese multiplicador: "))
producto = 0
for i in range(multiplicador):
    producto+=multiplicando
print("Resultado:", producto)