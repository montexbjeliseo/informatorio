"""
Realizar un programa que calcule y muestre la suma de los múltiplos 
de 5 comprendidos entre dos valores A y B. 
El programa no permitirá introducir valores negativos para A y B 
y verificará que A es menor que B. 
Si A es mayor que B, se deben intercambiar los valores.
"""
a = -1
b = -1
while(a<0):
    a = int(input("Ingrese valor para A (debe ser positivo): "))

while(b<0):
    b = int(input("Ingrese valor para B (debe ser positivo): "))

if a > b:
    desde = b
    hasta = a
else: 
    desde = a
    hasta = b
suma = 0
multiplos = 0
for i in range(desde, hasta+1):
    if i % 5 == 0:
        suma+= i
        multiplos+=1
print("Resultado:", suma)
print("Encontrados:", multiplos)