"""
Hacer un programa que imprima el nombre de un artículo, 
clave, precio original y su precio con descuento. 

El descuento lo hace en base a la clave, 
si la clave es 01 el descuento es del 10% 
y si la clave es 02 el descuento en del 20% 
(solo existen dos claves).
"""

nombre = input("Ingrese el nombre del artículo: ")
clave = input("Ingrese clave: ")
precio = float(input("Ingrese el precio: "))

print("*"*40)
print("Artículo")
print("Nombre:", nombre)
print("Clave:", clave)
print("Precio:", precio)

if clave == "01":
    print("Precio con descuento:", precio - precio * 0.1)
if clave == "02":
    print("Precio con descuento:", precio - precio * 0.2)
print("*"*40)