'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Reajuste salarial

'''

salario = float(input('Quanto está recebendo hoje? '))


if salario > 1250.00:
    reajuste = (salario * 0.10) + salario
    print('Reajuste de: \033[1;4;36mR${:.2f}\033[m'.format(salario * 0.10))
    print('Novo salário: \033[1;4;32mR${:.2f}\033[m'.format(reajuste))
else:
    reajuste = (salario * 0.15) + salario
    print('Reajuste de: \033[1;4;36mR${:.2f}\033[m'.format(salario * 0.15))
    print('Novo salário: \033[1;4;32mR${:.2f}\033[m'.format(reajuste))

