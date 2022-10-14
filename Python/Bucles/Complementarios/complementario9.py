"""
 Un censador recopila ciertos datos aplicando encuestas 
 para el último Censo Nacional de Población y Vivienda. 
 Desea obtener de todas las personas que alcance a encuestar en un día, 
 que porcentaje tiene estudios de primaria, secundaria, 
 carrera técnica, estudios profesionales y estudios de posgrado."""

vivo = True
encuestados = 0
registros = [0, 0, 0, 0, 0]
estudios = ["primaria", "secundaria", "tecnica", "profesionales", "posgrados"]
print("Ingrese \"c\" para terminar")
while(vivo):
    for i in range(len(estudios)):
        p = input("Posee estudios de "+estudios[i]+" (s para sí): ").lower()
        if p == "c":
            vivo = False
            break
        elif p == "s":
            registros[i]+=1
    encuestados+=1

print("Resultados:")
print("\tEncuestados:", encuestados)
print("\tPorcentaje primaria:", registros[0]/encuestados*100)
print("\tPorcentaje secundaria:", registros[1]/encuestados*100)
print("\tPorcentaje tecnica:", registros[2]/encuestados*100)
print("\tPorcentaje profesionales:", registros[3]/encuestados*100)
print("\tPorcentaje posgrado:", registros[4]/encuestados*100)