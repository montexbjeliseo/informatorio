ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto: "))

alt1 = True
for i in range(alto):
	linea = ""
	alt2 = True
	for j in range(ancho):
		if alt1:
			if alt2:
				linea+="*"
			else:
				linea+=" "
		else:
			if alt2:
				linea+=" "
			else:
				linea+="*"
		alt2 = not alt2
	print(linea)
	alt1 = not alt1
