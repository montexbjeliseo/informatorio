print("1: Primer receta")
print("2: Segunda receta")

recetas = ["primera", "segunda"]

escogida = int(input("Escojer: "))

ingredientes = [["verduras", "berenjena"], ["lentejas", "apio"], ["morrón", "cebolla"]]

print("1:", ingredientes[0][0])
print("2:", ingredientes[0][1])
print("3:", ingredientes[escogida][0])
print("4:", ingredientes[escogida][1])

ingredientes_escogidos = [0, 0, 0]

for i in range(0, 3):
	ingredientes_escogidos[i] = int(input("Ingrese un ingrediente: "))
	print(i, "=", ingredientes_escogidos[i])

print("Usted ha escogido la", recetas[escogida-1], "receta")
print("Ingredientes: ")

for ing in ingredientes_escogidos:
	if ing > 2:
		print(ingredientes[escogida][ing-3])
	else:
		print(ingredientes[0][ing-1])