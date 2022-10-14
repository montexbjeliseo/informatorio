"""
En un Centro Asistencial existen tres áreas: 
Pediatría, Traumatología y Kinesiología. 
El presupuesto anual del hospital se reparte conforme a la sig. tabla:

ÁREA 		  PORCENTAJE

Pediatría		 60%

Traumatología	 20%

Kinesiología	 20%


Obtener la cantidad de dinero que recibirá cada área, 
para cualquier monto presupuestal que se ingrese por teclado.
"""

presupuesto = float(input("Ingrese el presupuesto total: "))
area = int(input("1) Pediatría\n2) Traumatología\n3) Kinesiología\nIngrese: "))

if area == 1:
    print("El monto destinado a Pediatría será de:", presupuesto*0.6)
elif area == 2:
    print("El monto destinado a Traumatología será de:", presupuesto*0.2)
elif area == 3:
    print("El monto destinado a Kinesiología será de:", presupuesto*0.2)
else:
    print("No existe tal área")