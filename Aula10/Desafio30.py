'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: dizer se é par ou impar

'''
numero = int(input('Digite um número: '))
parImpar = numero % 2

if parImpar == 0 :
    print('{} é um número par'.format(numero))
else:
    print('{} é um número impar'.format(numero))