class Vehiculo:
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

class Coche(Vehiculo):
	def __init__(self, color, velocidad, cilindrada):
		super().__init__(color, 4)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

class Camioneta(Coche):
	def __init__(self, color, velocidad, cilindrada, carga):
		super().__init__(color, velocidad, cilindrada)
		self.carga = carga

class Bicicleta(Vehiculo):
	def __init__(self, color, tipo):
		super().__init__(color, 2)
		self.tipo = tipo

class Motocicleta(Bicicleta):
	def __init__(self, color, tipo, velocidad, cilindrada):
		super().__init__(color, tipo)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

vehiculos = []
vehiculos.append(Coche("Rojo", 250, 2993))
vehiculos.append(Camioneta("Azul", 250, 2993, 1000))
vehiculos.append(Bicicleta("Verde", "Urbana"))
vehiculos.append(Motocicleta("rojo", "Urbana", 70, 107))

def catalogar(lista):
	from pprint import pprint
	print("Vehiculos: %s" % (len(lista)))
	for v in lista:
		print("Tipo: %s" % (type(v).__name__))
		pprint(vars(v))

catalogar(vehiculos)