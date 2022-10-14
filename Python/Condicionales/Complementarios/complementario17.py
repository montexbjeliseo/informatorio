"""
Determinar y exhibir si la estatura de una persona adulta dada, 
es mayor que la estatura media de las personas adultas de su sexo, 
siendo:
- estatura media de mujeres adultas: 1,65 m.
- estatura media de varones adultos: 1,72 m.
"""

estatura = float(input("Estatura: "))
sexo = input("Sexo (m o f): ").upper()

if sexo == "M":
    if estatura > 1.72:
        superior = True
    else: 
        superior = False
else :
    if estatura > 1.65:
        superior = True
    else: 
        superior = False
if superior:
    print("La estatura es superior a la media de su sexo")
else:
    print("La estatura NO es superior a la media de su sexo")