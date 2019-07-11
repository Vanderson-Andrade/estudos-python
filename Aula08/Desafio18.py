'''

Recebe um valor em angulos e mostra o seno coseno e tangente

'''
from math import cos, tan, sin

angulo = float(input('Digite um ângulo: °'))
seno = sin(angulo)
coseno = cos(angulo)
tangente = tan(angulo)

print('Seno de {0}° = {1} \nCoseno de {0}° = {2} \nTangente de {0}° = {3}'.format(angulo, seno, coseno, tangente))