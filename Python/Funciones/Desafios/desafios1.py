"""
150 años es el tiempo que tarda una bolsa de plástico 
común en degradarse y una botella de PET puede tardar 
1.000 años en desaparecer. 

Por otro lado los Envases de tetrabrik pueden tardar 
hasta 30 años en degradarse.

Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, 
se solicite tipo: Bolsa de plástico, botella PET, 
envase tetrabrik o chicle, e imprima la cantidad de 
años que tarda en degradarse.
"""

def cuantoTarda(tipo):
    anios = 0
    if tipo == 1:
        anios = 150
    elif tipo == 2:
        anios = 30
    elif tipo == 3:
        anios = 5
    return anios

vivo = True

print("1) Plastico")
print("2) Tetrabrik")
print("3) Chicle")
while(vivo):
    tiempo = cuantoTarda(int(input("Ingrese tipo de material: ")))
    print("Tarda %s años en degradarse" % (tiempo))
    q = input("Continuar? (s - para sí): ").lower()
    if q != "s":
        vivo = False