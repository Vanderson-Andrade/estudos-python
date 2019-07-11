'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Programa que ler um numero de 0 a 9999 e mostra cada uma das casas decimeis: unidade, dezena, centena, milhar

'''
num = str(input('Digite um número entre 0 e 9999: '))
print('''
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
'''.format(num[3], num[2], num[1], num[0]))