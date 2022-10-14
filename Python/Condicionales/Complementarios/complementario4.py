#Realizar un programa que sea capaz de, 
# habiéndose ingresado dos números m y n, 
# determine si n es divisor de m

m = int(input("Ingrese un valor para n: "))
n = int(input("Ingrese un valor para m: "))

if m % n == 0:
    print("%s es dividor de %s" % (n, m))
else: 
    print("%s es NO dividor de %s" % (n, m))