#Solicitar el ingreso de números al usuario y 
# emitir un mensaje para determinar si es par o impar. 
# El ciclo debe finalizar cuando el usuario ingresa 0.

vivo = True

while(vivo):
    num = int(input("Ingrese un valor: "))
    if num == 0:
        print("Finalizar")
        vivo = False
    else: 
        if num % 2 == 0:
            print("El numero ingresado es par")
        else:
            print("El numero ingresado es impar")