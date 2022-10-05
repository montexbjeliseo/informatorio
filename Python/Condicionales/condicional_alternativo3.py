nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (m o f): ")
grupo = "";

if sexo.lower() == "f":
	if nombre.lower() < "m":
		grupo = "A";
	else :
		grupo = "B"
elif sexo.lower() == "m":
	if nombre.lower() > "n":
		grupo = "A";
	else :
		grupo = "B"

print(nombre, "pertenece al grupo", grupo)