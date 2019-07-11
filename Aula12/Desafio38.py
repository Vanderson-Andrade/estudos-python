'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Maior e menor
'''
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

if n1 > n2:
    print('O número {} é maior'.format(n1))
    print('O número {} é menor'.format(n2))
elif n1 < n2:
    print('O número {} é maior'.format(n2))
    print('O número {} é menor'.format(n1))
else:
    print('Não existe um valor maior, os dois são iguais!')