"""
Calcular el monto a pagar por cada cliente y total recaudado 
en una estación de servicio. 
Debe diseñar un programa que permita monto por cliente y 
el total recaudado por la gasolinera, tomando en cuenta lo siguiente:

• El precio del litro es para el Tipo A $50, 
  para el Tipo B $ 55 y para el Tipo C $60

• El programa finaliza cuando se introduce una D 
  como tipo de gasolina.
"""
print("Ingrese \"D\" para detener")
vivo = True
recaudado = 0
while(vivo):
    entradas = ["tipo", "litros"]
    valores = [0, 0]
    for i in range(len(entradas)):
        entrada = input("Ingrese "+entradas[i]+": ").lower()
        if entrada == "d":
            vivo = False
            break
        else :
            if i == 0:
                if entrada == "a":
                    valores[0] = 50
                elif entrada == "b":
                    valores[0] = 55
                elif entrada == "c":
                    valores[0] = 60
            if i == 1:
                valores[1] = float(entrada)
    if vivo:
        total = valores[0]*valores[1]
        recaudado+=total
        print("Total a pagar:", total)
print("Recaudado:", recaudado)