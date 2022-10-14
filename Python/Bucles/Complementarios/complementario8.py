# Diseñar un programa que permita calcular el total de una compra, 
# ingresando cantidad y precio de los productos. 
# El programa debe estar preparado para que el ingreso de los datos 
# se produzca hasta que el usuario lo desee.

print("Ingrese \"0\" para terminar")
vivo = True
suma = 0

while(vivo):
    cantidad = int(input("Cantidad: "))
    if cantidad == 0:
        vivo = False
        break
    precio = float(input("Precio: "))
    suma += precio * cantidad
print("Total:", suma)