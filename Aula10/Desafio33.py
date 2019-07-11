'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: ler 3 numero e mostrar o maior eo menor numero

'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
n3 = int(input('Digite um ultimo número: '))

if n1 > n2 and n1 > n3:
    print('Maior: {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('Maior: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('Maior: {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('Menor: {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('Menor: {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('Menor: {}'.format(n3))