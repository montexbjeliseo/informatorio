"""
Una pizzería, vende sus pizzas en tres tamaños: 
pequeña, mediana; y grandes. Una pizza puede ser sencilla 
(con sólo salsa y carne), o con ingredientes extras, 
tales como pepinillos, champiñones o cebollas. 
Desarrolle una solución que calcule el precio de venta de una pizza, 
dándole el tamaño y el número de ingredientes extras. 
El precio de venta será 1.5 veces el costo total, 
que viene determinado por el tamaño, más el número de ingredientes. 
En particular el costo total se calcula sumando:

- un costo fijo de preparación.

- un costo variable que es proporcional al tamaño de la pizza.

- un costo adicional por cada ingrediente extra 
(por simplicidad se supone que cada ingrediente extra 
tiene el mismo costo).
"""

vivo = True
FIJO = 100 #Pequeña
print("Para cerrar ingrese \"c\"")

while(vivo):
	precio = FIJO
	tamanio = int(input("Ingrese 1 - Pequeña, 2 - Mediana, 3 - Grande: "))
	if tamanio == 1:
		pass
	elif tamanio == 2:
		precio *= 1.3
	elif tamanio == 3:
		precio *= 1.5
	else :
		continue

	pepinillos = input("Pepinillos? (s - para sí): ").lower()
	if pepinillos == "s":
		precio += 25
	champinioones = input("Champiñones? (s - para sí): ").lower()
	if champinioones == "s":
		precio += 25
	cebollas = input("Cebollas? (s - para sí): ").lower()
	if cebollas == "s":
		precio += 25

	precio *= 1.5
	print("Precio final:", precio)

	if input("Seguir? (s - para sí): ").lower() != "s":
		vivo = False
		print("Finalizar!")