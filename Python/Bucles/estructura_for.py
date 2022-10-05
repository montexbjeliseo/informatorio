from random import randrange

print("Bienvenido!")

multiplicaciones = int(input("Ingrese la cantidad de multiplicaciones: "))

aciertos = 0

for i in range(0, multiplicaciones):
	multiplicador = randrange(2, 10)
	multiplicando = randrange(2, 10)

	resultado = multiplicador * multiplicando

	respuesta = int (input("Ingrese el resultado de "+str(multiplicador)+"*"+str(multiplicando)+": "))

	if int(resultado) == respuesta:
		aciertos+=1

print("Cantidad multiplicaciones:", multiplicaciones)
print("Cantidad de aciertos:", aciertos)
print("Porcentaje de aciertos:", aciertos / multiplicaciones * 100)
print("Porcentaje de desvío:", 100 - aciertos / multiplicaciones * 100)