matorrales = input("Existen matorrales? ( S para sí y N para no): ")

if(matorrales.lower()=="s"):
	matorrales = True
else :
	matorrales = False

terreno = float(input("Hectareas de suelo: "))
compuesto = float(input("Cantidad de compuesto; "))

if matorrales or compuesto <= terreno * 0.1:
	print("No es factible su uso")
else :
	print("Su uso es factible")