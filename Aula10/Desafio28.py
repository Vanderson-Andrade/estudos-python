'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: criar um programa que pense em um numero de 0 a 5 e peça para o usuario tentar acertar o numero escolhido

'''
import random
numero = random.randint(0,5)
tentativa = int(input('''
***** Jogo de adivinhação *****
Digite um número de 0 a 5: '''))

if tentativa == numero :
    print('Parabens! você acertou')
else:
    print('Que pena, tente de novo')