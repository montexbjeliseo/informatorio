"""
Hacer un programa que calcule el total a pagar 
por la compra de camisas. Si se compran tres camisas 
o mas se aplica un descuento del 20% sobre el total de la compra 
y si son menos de tres camisas un descuento del 10%.
"""
precio = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad: "))
total = precio * 3
if cantidad >= 3:
    total -= precio * 3 * 0.2
else :
    total -= precio * 3 * 0.1

print("Total a pagar:", total)