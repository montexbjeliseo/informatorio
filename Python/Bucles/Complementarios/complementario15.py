"""
En un supermercado se hace una promoción, mediante la cual el cliente 
obtiene un descuento dependiendo de un número que se escoge al azar. 
Si el número escogido es menor que 50 el descuento es del 15% 
sobre el total de la compra, si es mayor o igual a 50 el descuento es del 20%. 
Obtener cuánto dinero se le descuenta.
"""
from random import randrange

vivo = True

while(vivo):
	precio = float(input("Ingrese el importe: "))
	num = randrange(0, 100)
	if num < 50:
		descuento = 15
	elif num >= 50:
		descuento = 20
	else :
		descuento = 0
	final = precio - precio * descuento / 100 
	print("Total a pagar:", final)
	print("Obtuvo un descuento de: " + str(descuento) + "%")
	q = input("Continuar? (s - para sí): ").lower()
	if q != "s":
		vivo = False