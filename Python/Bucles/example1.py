'''
Encontrar todas las cifras de 3 dígitos
en cuales la suma de los cubos de sus dígitos
sean igual a dicha cifra
'''

for i in range(100, 1000):
	c = i // 100
	d = (i // 10) % 10
	u = i % 10

	if (c**3 + d**3 + u**3) == i:
		print("Cumple: ", i)

print("-----------------------------------------")

for i in range(100, 1000):
	s = str(i)
	suma = 0
	for x in s:
		suma+=int(x)**3
	if suma == i:
		print("Cumple: ", i)