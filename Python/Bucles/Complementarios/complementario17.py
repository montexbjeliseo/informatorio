"""
Calcular la utilidad que un trabajador recibe en el reparto anual 
de utilidades si este se le asigna como un porcentaje de su salario mensual 
que depende de su antigüedad en la empresa de acuerdo con la sig. tabla:

Tiempo											Utilidad

Menos de 1 año									5% del salario

Más de 1 año y hasta 2 años		 				7% del salario

Más de 2 años y hasta 5 años 					10% del salario

Más de 10 años								 	20% del salario
"""
vivo = True
while(vivo):
	salario = int(input("Ingrese salario: "))
	print("1 - Menos de 1 año")
	print("2 - Más de 1 años y hasta 2 años")
	print("3 - Más de 2 años y hasta 5 años")
	print("4 - Más de 10 años")
	antig = int(input("Años de antigüedad: "))
	if antig == 1:
		utilidad = salario * 1.05
	elif antig == 2:
		utilidad == salario * 1.07
	elif antig == 3:
		utilidad = salario * 1.10
	elif antig == 4:
		utilidad = salario * 1.20
	else :
		print("Error")
		continue
	print("Utilidad:", utilidad)
	q = input("Continuar? (s - para sí): ").lower()
	if q != "s":
		vivo = False