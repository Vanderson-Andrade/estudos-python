'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Jokenpô

'''

#IMPORTAÇÕES
from random import randint
from time import sleep

# CABEÇALHO
print('\033[36;1m*=\033[m'*13)
titulo = ' JOKENPÔ '
print('\033[33m{:*^40}'.format(titulo))
print('\033[36;1m*=\033[m'*13)
print('''                REGRAS:
PEDRA GANHA DA TESOURA E PERDE PARA O PAPEL.
PAPEL GANHA DA PEDRA E PERDE PARA TESOUA.
TESOURA GANHA DO PAPEL E PERDE PARA PEDRA.
----------------------------------------
                OPÇÕES:
PEDRA   -> [ 1 ]
PAPEL   -> [ 2 ]
TESOURA -> [ 3 ]
----------------------------------------''')

# lOGICA DO JOGO
escolha = int(input('Faça sua jogada: '))
print('')
maquina = randint(1,3)

opcoes = 'PEDRA PAPEL TESOURA'
opcoes = opcoes.split()

if escolha <= 3 and escolha >= 1:
    print('             JO* * * * * *')
    sleep(1)
    print('             * * *KEN* * *')
    sleep(1)
    print('             * * * * * *PÔ!\n')

    print('COMPUTADOR: {} -VS- JOGADOR: {}\n'.format(opcoes[maquina - 1], opcoes[escolha - 1]))

#---------------------------------------------------------
    msg1 = '\033[32;1m VOCÊ GANHOU! \033[m'
    msg2 = '\033[31;1m VOCÊ PERDEU! \033[m'
    msg3 = '\033[33m EMPATE! \033[m'

    if maquina == escolha:
        print('{:*^48}'.format(msg3))
    #pedra
    elif maquina == 1 and escolha == 3:
        print('{:*^50}'.format(msg2))
    elif maquina == 1 and escolha == 2:
        print('{:*^50}'.format(msg1))

    #papel
    elif maquina == 2 and escolha == 1:
        print('{:*^50}'.format(msg2))
    elif maquina == 2 and escolha == 3:
        print('{:*^50}'.format(msg1))
    #tesoura
    elif maquina == 3 and escolha == 2:
        print('{:*^50}'.format(msg2))
    elif maquina == 3 and escolha == 1:
        print('{:*^50}'.format(msg1))
else:
    print('\033[33mOPÇÃO INVÁLIDA TENTE NOVAMENTE !')




