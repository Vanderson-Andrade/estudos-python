'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Diz de a pessoa tem silva no nome

'''
nome = str(input('Digite seu nome completo: '))
nome = nome.upper()
print('Tem silva em seu nome: {}'.format('SILVA' in nome))