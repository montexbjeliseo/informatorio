"""
Crea un diccionario donde la clave sea el nombre de biólogos y el valor 
sea el email (no es necesario validar). 
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere 
insertar mas. No se podrán insertar nombres repetidos.
"""

biologos = {}

vivo = True

while(vivo):
    nombre = input("Ingrese nombre: ")
    if biologos.get(nombre)!=None:
        print("Ya existe este nombre")
        continue
    email = input("Ingrese email")
    biologos[nombre]=email
    q = input("Continuar? (s - para sí): ").lower()
    if q != "s":
        vivo = False
print("Resultados:", biologos)