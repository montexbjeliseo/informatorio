precio = float(input("Ingrese el precio por unidad: "))
unidades = int(input("Ingrese las unidades: "))

if unidades >= 10:
	total = unidades * precio * 80 / 100
else :
	total = unidades * precio

print("El precio total de compra es: ", total)