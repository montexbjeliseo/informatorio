"""
 Escribir un programa el cual lea dos valores enteros. 
 Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''. 
 Si el segundo es menor que el primero, que imprima el mensaje ``Abajo''. 
 Si los números son iguales, que imprima el mensaje ``igual''. 
 Si alguno de los datos ingresados es igual a 0, que imprima un mensaje 
 conteniendo la palabra ``Error''.
"""

vivo = True

while(vivo):
	num1 = int(input("Ingrese primer numero: "))
	if num1 == 0:
		print("Error")
		continue
	num2 = int(input("Ingrese segundo numero: "))
	if num2 == 0:
		print("Error")
		continue
	
	if num1 == num2:
		print("Igual")
	elif num1 < num2 :
		print("Arriba")
	else : 
		print("Abajo")

	q = input("Continuar? (s - para sí): ").lower()

	if q != "s":
		vivo = False