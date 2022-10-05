personas = int(input("Ingrese la cantidad de personas que recogen colillas: "))

colillas = []

for i in range(personas):
	colillas.append(int(input("Ingrese la cantidad de colillas recolectadas por la persona"+str(i)+": ")))

mas_de200 = 0
menos_de200 = 0
menos_de100 = 0

total_colillas = 0

for recolectadas in colillas:
	total_colillas+=recolectadas

for recolectadas in colillas:
	if recolectadas >= 200:
		mas_de200+=1
	elif recolectadas < 200:
		menos_de200+=1
	elif recolectadas < 100:
		menos_de100+=1

print("Participaron", personas, "personas en la recolección")
print("Se recolectaron", total_colillas, "colillas")
print(mas_de200, "personas recolectaron más de 200")
print(menos_de200, "personas recolectaron más de 100")
print(menos_de100, "personas recolectaron menos de 100")
