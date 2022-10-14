"""
Una distribuidora de libros vende a librerías y a particulares. 
Aplica bonificaciones por cantidad según el siguiente criterio:

    i. a librerías: hasta 24 unidades, el 20%; más de 24 unidades, 
    el 25%.

    ii. a particulares: menos de 6 unidades, nada; desde 6 hasta 
    18 unidades, el 5% y más de 18 unidades, el 10%.

El tipo de cliente está codificado así: 'L' para librerías, 
'P' para particular. Dado el importe bruto de una compra de libros, 
el tipo de cliente de que se trata y la cantidad total pedida 
por el mismo, determinar el importe bruto bonificado.
"""

unidades = int(input("Unidades: "))
precio =  float(input("Precio: "))
cliente = input("Cliente (L o P)").upper()
descuento = 0
if cliente == "L":
    if unidades <= 24:
        descuento = 20
    else :
        descuento = 25
else :
    if 6 >= unidades <= 18:
        descuento = 5
    elif unidades > 18:
        descuento = 10
total = unidades * precio
ahorro = total * descuento / 100
final = total - ahorro
print("Total a pagar:",  final)
print("Bonificación:", ahorro)