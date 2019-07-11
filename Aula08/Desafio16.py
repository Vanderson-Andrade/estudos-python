'''
Ler um numero e mostra sua porção inteira

'''
from math import trunc
# import math

num = float(input('Digite um numero: '))
print('O número {} tem a parte inteira: {}'.format(num, trunc(num)))