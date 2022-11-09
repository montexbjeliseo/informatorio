class Triangulo:
	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

class Equilatero(Triangulo):
	def __init__(self, longitud):
		super().__init__(longitud, longitud, longitud)

class Isoceles(Triangulo):
	def __init__(self, lado1, lado2):
		super().__init__(lado1, lado2, lado2)

class Escaleno(Triangulo):
	def __init__(self, lado1, lado2, lado3):
		super().__init__(lado1, lado2, lado3)

triangulos = []
triangulos.append(Equilatero(100));
triangulos.append(Isoceles(100, 50))
triangulos.append(Escaleno(150, 100, 50))

from pprint import pprint

for t in triangulos:
	print("Tipo: %s" % (type(t).__name__))
	pprint(vars(t))
