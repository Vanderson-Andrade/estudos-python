'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: emprestimo bancario para compra de uma casa

'''
nome = str(input('Nome: '))
salario = float(input('Salário: R$'))
vcasa = float(input('Valor do emprestimo: R$'))
tempoano = int(input('Quantos anos para pagar: '))

prestacao = vcasa / (tempoano*15)

if prestacao > (salario * 0.30):
    print('\033[31;1;4mInfelizmente não podemos liberar seu emprestimo no momento.\033[m')
elif prestacao < (salario * 0.30):
    print('\033[32mSeu emprestimo foi aprovado, verifique seu saldo.\033[m')
