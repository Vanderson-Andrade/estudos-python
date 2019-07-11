'''

ler dois catetos de um triangulo retangulo e mostra sua hipotenusa

'''
from math import hypot

catOposto = float(input('Digite o valor do cateto oposto: '))
catAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipo = hypot(catOposto, catAdjacente)
print("Hipotenusa = {}".format(hipo))
