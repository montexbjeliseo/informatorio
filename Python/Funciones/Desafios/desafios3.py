"""
Realiza una función separar(lista) que tome una lista que tenga datos 
de cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena. 
Luego la función debe devolver dos listas ordenadas. 
La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
"""
def separar(lista):
    mas100 = []
    resto = []
    for i in lista :
        if i[1] > 100:
            mas100.append(i)
        else :
            resto.append(i)
    return [mas100, resto]
lista1 = [["Chaco", 101], ["BS", 200], ["Jujuy", 150], ["Mendoza", 50]]
separado = separar(lista1)
print("Mas de 100:", separado[0])
print("Resto:", separado[1])