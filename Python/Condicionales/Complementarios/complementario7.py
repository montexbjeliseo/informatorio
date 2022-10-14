"""
Un comercio ofrece un descuento del 15% sobre el total de la compra 
si esta supera los $1000. 
Obtenga para determinado cliente cuánto deberá pagar finalmente 
por su compra y el descuento obtenido, si es que corresponde.
"""

monto = float(input("Ingrese el monto de la compra: "))
final = monto
if monto > 1000:
    descuento = monto * 15 / 1000
    final-= descuento
    print("Obtiene 15% de descuento:", descuento)
    
print("El cliento debe pagar:", final)