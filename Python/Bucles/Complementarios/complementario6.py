# Imprimir, contar y sumar los múltiplos de 2 
# que hay entre una serie de números, tal que el segundo 
# sea mayor o igual que el primero.
desde = int(input("Desde: "))
hasta = int(input("Hasta: "))
multiplos = 0
suma = 0
for i in range(desde, hasta+1):
    if i % 2 == 0:
        print(i)
        suma+=i
        multiplos+=1
print("Encontrados:", multiplos)
print("Suma:", suma)