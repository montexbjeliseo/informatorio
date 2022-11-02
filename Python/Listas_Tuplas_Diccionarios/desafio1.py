"""
Escribir un programa que pregunte a diferentes personas cuánto conocen 
sobre contaminación del 1 al 10, almacene estos valores en una lista y 
los muestre por pantalla ordenados de menor a mayor.
"""
encuestados = []
def encuestar():
    nombre = input("Ingrese su nombre")
    conocen = input("Cuánto conocen de contaminación del 1 a l 10: ")
    encuestados.append({"nombre" : nombre, "conocen" : conocen})
vivo = True
while(vivo):
    encuestar()
    q = input("Continuar? (s - para sí): ").lower()
    if q != "s":
        vivo = False
        print("Resultados:", sorted(encuestados, reverse=true, key=lambda persona : persona["conocen"]))