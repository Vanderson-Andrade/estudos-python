'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Ler a velocidade de um carro e diz se ele foi multado por velocidade e mostra o valor da multa
'''

kmPermitido = 80
velocidadeCarro = float(input('Qual a velocidade do Carro em KM/H: '))

if velocidadeCarro > kmPermitido:
    valorMulta = (velocidadeCarro - kmPermitido) * 7.0
    print('Você exedeu o limite permitido de velocidade')
    print('Valor da multa: R${:.2f}'.format(valorMulta))
else:
    print('Dentro do limite de 80Km/h')