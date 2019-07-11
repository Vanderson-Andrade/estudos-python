'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição:

'''
import math
numero = int(input('Digite um número: '))
opcao = int(input('''
-=-=-=-=-=-=-=-=-=-=-=-=
    ESCOLA UMA OPÇÃO
-=-=-=-=-=-=-=-=-=-=-=-=
1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL
-=-=-=-=-=-=-=-=-=-=-=-=
        OPÇÃO: '''))
if opcao == 1:
    print('{} em BINÁRIO é = {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} em OCTAL é = {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} em HEXADECIMAL é = {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida tente novamente! ')