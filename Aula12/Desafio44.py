'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição:fluxo de caixa

'''
print('\033[36;1m*=\033[m'*20)
titulo = ' Análise de Pagamentos '
print('\033[33m{:*^40}'.format(titulo))
print('\033[36;1m*=\033[m'*20)

valor = float(input('Valor do produto: \033[32mR$\033[m'))
opcao = int(input('''
Escolha uma forma de pagamento
[ 1 ] -> Dinheiro/Cheque
[ 2 ] -> Cartão de Credito
Opção: '''))

if opcao == 1:
    desconto = valor - (valor * 0.1)
    print('Pagamento a vista: {}'.format(desconto))
elif opcao == 2:
    opcao = int(input('''
    Cartão de Credito
    [ 1 ] -> Avista
    [ 2 ] -> Parcelado
    Opção: '''))
    if opcao == 1:
        desconto = valor - (valor * 0.05)
        print('Pagamento a vista: {}'.format(desconto))
    elif opcao == 2:
        vezes = int(input('Quantas vezes: x'))
        if vezes <= 2:
            print('Valor da parcela: R${}'.format(valor / vezes))
            print('Total a pagar: R${}'.format(valor))
        elif vezes > 2:
            valor = valor + (valor * 0.2)
            print('Valor da parcela: R${}'.format(valor / vezes))
            print('Valor total: R${}'.format(valor))