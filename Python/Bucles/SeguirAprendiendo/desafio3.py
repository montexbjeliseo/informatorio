abierto = True

while abierto:
	entrada = input("Ingrese: cerrar o cantidad de tapitas para calcular descuento: ")
	if entrada.lower() == "cerrar":
		abierto = False
	else: 
		tapitas = int(entrada)
		descuento = 0
		if tapitas >= 1000:
			print("descuento de 40%")
			descuento = 40
		elif tapitas > 500:
			print("descuento de 25%")
			descuento = 25
		else :
			print("No alcanza para un descuento")
			descuento = 0
		importe = float(input("Ingrese el importe de la compra: "))
		print("Debe pagar", importe - importe * descuento / 100)
print("Fin del programa")