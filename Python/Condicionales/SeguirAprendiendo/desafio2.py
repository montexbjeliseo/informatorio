print("Elija una opción")
print("1: Pez tamaño pequeño")
print("2: Pez tamaño normal")
print("3: Pez tamaño por encima de lo normal")
print("4: Pez tamaño muy por encima de lo normal")

opcion = int(input(""))

if opcion==1:
	print("Peces con problemas de nutrición")
elif opcion == 2:
	print("Peces saludables")
elif opcion == 3:
	print("Peces posiblemente afectados por contaminación")
elif opcion == 4:
	print("Peces contaminados!")
else :
	print("Opción incorrecta")