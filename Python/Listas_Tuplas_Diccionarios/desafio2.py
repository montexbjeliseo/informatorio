"""
Crea una tupla con los factores que más afectan a los mares. 
Luego para jugar con niños y niñas, aprendiendo sobre contaminación 
del agua crea un programa que pida números, 
si el numero esta entre 1 y la longitud máxima de la tupla, 
muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.
"""
vivo = True
factores = ("Las aguas residuales", "Las sustancias químicas tóxicas", "Las aguas pluviales", \
    "El vertido de plásticos", "Los vertidos de petróleo", "La actividad minera en alta mar", \
        "El cambio climático")
while(vivo):
    num = int(input("Ingrese un numero entre 1 y %s: " % (len(factores))))
    if num == 0:
        vivo = False
        print("Finalizar")
    elif num > len(factores):
        print("Error!")
    else :
        print(factores[num-1])