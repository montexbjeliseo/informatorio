edad = int(input("Ingrese su edad: "))

if edad < 18 and edad >= 0:
	print("Eres menor de edad.")
elif edad >= 18:
	print("Eres mayor de edad")
else :
	print("Ni siquiera has nacido")
