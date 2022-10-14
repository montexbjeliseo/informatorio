#Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))
num3 = int(input("Ingrese tercer número: "))
linea = ""
if num2 < num1 > num3:
    linea+=str(num1)
    if num2 > num3:
        linea+=", " + str(num2) + ", " + str(num3)
    else :
        linea+=", " + str(num3) + ", " + str(num2)
elif num1 < num2 > num3 :
    linea+=str(num2)
    if num1 > num3:
        linea+=", " + str(num1) + ", " + str(num3)
    else :
        linea+=", " + str(num2) + ", " + str(num1)
else :
    linea+=str(num3)
    if num1 > num2:
        linea+=", " + str(num1) + ", " + str(num2)
    else :
        linea+=", " + str(num2) + ", " + str(num1)
print("Mayor a menor: ", linea)