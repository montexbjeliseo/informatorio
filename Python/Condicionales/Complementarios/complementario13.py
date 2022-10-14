"""
En un supermercado se hace una promoción, mediante la cual el cliente 
obtiene un descuento dependiendo de un número que se escoge al azar. 
Si el numero escogido es menor que 74 el descuento es del 15% 
sobre el total de la compra, si es mayor o igual a 74 el descuento 
es del 20%. Obtener cuánto dinero se le descuenta.
"""
from random import randint as aleatorio_entre
monto = float(input("Ingrese el monto de compra: "))
num = aleatorio_entre(0, 100)
final = monto
if num < 74:
    descuento = 15
elif num >= 74:
    descuento = 20
ahorrado= monto * descuento / 100
final -= ahorrado
print("*"*40)
print("Importe:", monto)
print("Total a pagar:", final)
print("Descuento obtenido:", ahorrado)
print("Porcentaje de descuento:", descuento)