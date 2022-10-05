clave = 1234
ingresada = int()
intentos = 3
pase = False

while(not pase):
	ingresada = int(input("Ingrese la clave: "))
	if ingresada == clave:
		pase = True
	else :
		intentos-=1
		if intentos == 0:
			print("Se acabaron los intentos")
			break
		else:
			print("Clave incorrecta, te quedan", intentos, "intentos")
	
	if pase:
		print("Verificación exitosa")

print("Fin del programa")