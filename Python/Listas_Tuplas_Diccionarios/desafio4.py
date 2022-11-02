"""
Escribir un programa que cargue una tupla con nombres de especie, 
y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.

Modificá el programa anterior y dada una posición inicial p y una cantidad n, 
imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición i.
"""
especies = ("HUEMUL", "YAGUARETÉ", "AGUARÁ GUAZÚ", "BALLENA FRANCA AUSTRAL", \
    "CÓNDOR ANDINO", "TATÚ CARRETA", "PINGÜINO DE MAGALLANES", "PECARÍ DEL CHACO", \
        "MONO CAÍ O CAPUCHINO", "CIERVO DE LOS PANTANOS", "SURI CORDILLERANO O ÑANDÚ", \
            "VENADO DE LAS PAMPAS", "CARAYÁ-PITÁ (MONO AULLADOR)", "FLAMENCO ANDINO", \
    "TAPIR", "GUACAMAYO VERDE", "OSO HORMIGUERO GIGANTE", "HUILLÍN", "CAUQUÉN COLORADO", \
        "RANA TELMATOBIUS ATACAMENSIS")
print("cantidad de registros:", len(especies))
p = int(input("Posicion ingrese: "))
n = int(input("Cantidad: "))
for i in range(p, p+n):
    print("Hola soy", especies[i], "cuidame!")