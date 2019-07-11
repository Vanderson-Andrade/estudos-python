'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Ler um nome e mostra seu primeiro e seu ultimo nome

'''
nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.split()
print('Primero nome: {}'.format(nome1[0]))
print('Ultimo nome: {}'.format(nome1[len(nome1)-1]))