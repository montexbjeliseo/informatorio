class Tiempo:
	def __init__(self, horas, minutos, segundos):
		self.__horas = horas
		self.__minutos = minutos
		self.__segundos = segundos

	def set_horas(self, horas):
		self.__horas = horas
	def get_horas(self):
		return self.__horas
	def set_minutos(self, minutos):
		self.__minutos = minutos
	def get_horas(self):
		return self.__horas
	def set_segundos(self, segundos):
		self.__segundos = segundos
	def get_segundos(self):
		return self.__segundos

class Prueba_Tiempo(Tiempo):
	def __init__(self, horas, minutos, segundos):
		super().__init__(horas, minutos, segundos)

from pprint import pprint

prueba = Prueba_Tiempo(1, 44, 2022)

pprint(vars(prueba))
prueba.set_horas(7)
pprint(vars(prueba))