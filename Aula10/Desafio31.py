'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: calcular o preço de uma passagem

'''
distancia = float(input('qual a distancia em km de sua viagem: '))

if distancia <= 200 :
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print('Valor da viagem: R${:.2f}'.format(preco))
