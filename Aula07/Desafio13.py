'''
= = = = = Descrição = = = = =

Programa que ler o salario de um funcionario de mostra seu novo salario com 15% de almento

'''
salario = float(input('Digite seu salário: '))
novoSalario = salario +(salario * 0.15)
print('Salário com almento: {}'.format(novoSalario))