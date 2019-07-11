'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: imc

'''
altura = float(input('Altura em cm: '))
peso = float(input('Peso em Kg: '))

imc = peso / pow(altura, 2.0)

print('imc = {:.1f}'.format(imc))

