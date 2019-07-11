'''
= = = = = Descrição = = = = =

Programa que ler quanto de dinheiro em reais a pessoa tem e converte para U$

considerando U$ valendo = 3,27R$

'''

carteira = float(input('Quanto tem em sua carteira: '))
dola = carteira / 3.27
print('='*20)
print('Valor em dólares: ${:.2f}'.format(dola))