"""
Mostrar los perímetros de varios triángulos ingresados sus lados 
por teclado, hasta que ya no desee.
"""
print("Ingrese \"c\" para terminar")
vivo = True

while(vivo):
    perimetro = 0
    for i in range(3):
        entrada = input("Ingrese longitud "+str(i+1)+"°: ").lower()
        if entrada == "c":
            vivo = False
            break
        else:
            perimetro += int(entrada)
    if vivo:
         print("Perímetro:", perimetro)