nombre = input("Nombre del barrio: ").lower()
centrico = input("Está en zona céntrica? (s para sí): ")

if centrico.lower() == "s":
	centrico = True
else :
	centrico = False
if centrico and nombre[0] < "m" or not centrico and nombre[0] > "m":
	print("Seccion A")
else :
	print("Seccion B")