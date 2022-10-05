importe = float(input("Ingrese el importe: "))

mensaje = "Lo sentimos, no hay descuentos"

if importe >= 1500:
	mensaje = "Descuento de 30%" + "\nDebe pagar: " + str(importe * 0.7)
elif importe >= 750:
	mensaje = "Descuento de 20%" + "\nDebe pagar: " + str(importe * 0.8)
elif importe >= 350:
	mensaje = "Descuento de 10%" + "\nDebe pagar: " + str(importe * 0.9)

print(mensaje)