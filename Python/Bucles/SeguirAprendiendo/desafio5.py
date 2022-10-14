"""Se está desarrollando un sistema de control de vehículos 
desde donde se han tirado restos de basura a la vía pública.

Para ello la ciudad cuenta con sistemas de monitoreo de patentes 
que devuelve 3 letras y un valor numérico de 5 dígitos a la Central 
con el siguiente significado:

3 letras: Correspondientes a la patente.

Del valor numérico:

    Los 3 primeros números corresponden a la patente

    El 4 número indica

    1- Tiró basura a la vía pública

    0 - No tiró basura a la vía pública

El 5 número indica

    1- Ya había sido multado el vehículo

    0 - Vehículo sin multas.

ABC 123 1 0 // Tiró basura a la vía pública, Vehículo sin multas.

Deberás informar cantidad de vehículos observados, cantidad de vehículos 
que han tirado basura y porcentaje de éstos que ya habían sido multados.
"""
print("\n", "*"*40, "\n")
print("\tBienvenido(és només una proposta)!\n")
print("\n", "*"*40, "\n")
observados = int(input("Ingrese la cantidad de vehiculos observados: "))
tiraron_basura = 0
multados = 0
print("\n", "*"*40, "\n")
print("Ingrese 3 letras y 3 numeros de la patente")
print("Ingrese 1 para indicar que arrojó basura, de lo contrario 0")
print("Ingrese 1 para indicar que tiene multasm de lo contrario 0")
print("Por ejemplo: ABC12310")

for i in range(observados):
    entrada = input("Ingrese los datos:")
    if entrada[6] == "1":
        tiraron_basura += 1
    if entrada[7] == "1":
        multados += 1

print("\n", "*"*40, "\n")
print("* Vehiculos observados:")
print("\t- Total:", observados)
print("* Vehiculos que arrojaron basura:")
print("\t- Total:", tiraron_basura)
print("\t- Porcentaje respecto de observados:", tiraron_basura / observados * 100, "%")
print("* Vehiculos multados:")
print("\t- Total:", multados)
print("\t- Porcentaje respecto de observados:", multados / observados * 100, "%")
print("\t- Porcentaje respecto de los que arrojaron basura:", multados / tiraron_basura * 100, "%")