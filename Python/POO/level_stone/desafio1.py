class Vehiculo:
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

class Auto(Vehiculo):
	def __init__(self, color, velocidad, cilindrada):
		super().__init__(color, 4)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def toString(self):
		texto = "*"*40
		texto += "\nColor: "
		texto += self.color
		texto += "\nRuedas: "
		texto += str(self.ruedas)
		texto += "\nVelocidad max: "
		texto += str(self.velocidad)
		texto += "\nCilindrada: "
		texto += str(self.cilindrada)
		return texto

auto1 = Auto("rojo", 250, 2993)
print(auto1.toString())