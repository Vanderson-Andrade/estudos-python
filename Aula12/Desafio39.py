'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: idade de alistamento

'''
from datetime import date

nome = str(input('Nome completo: '))
nome1 = nome.split()
ano = int(input('Ano de nascimento: '))
sexo = str(input('Qual seu sexo? (M) = Masculino e (F) = Feminino: '))
sexo = sexo.upper()
atual = date.today().year
idade = atual - ano

if sexo != 'M' and sexo != 'F':
    print('\033[31;1mOpção de sexo invalida, tente novamente informando uma opção valida')

else:
    print('-='*20)
    print('Olá \033[34;1m{}\033[m! você tem \033[34;1m{}\033[m anos.'.format(nome1[0].upper(), idade))

    if sexo == 'F':
        print('\033[34;1mE de acordo com a lei você não precisa se alistar.')

    elif idade > 18:
        passou = idade - 18
        anoalistamento = atual - passou
        print('\033[34;1mVocê já passou do tempo de alistamento. Seu ano de alistamento era \033[31;1;4m{} anos atras em {}\033[34;1m !!!'.format(passou,anoalistamento))

    elif idade == 18:
        print('\033[34;1mE esse ano é seu ano de alistamento. \033[32;1;4mNÂO PERCA TEMPO!')

    else:
        falta = 18 - idade
        anoalistamento = atual + falta
        if falta > 1:
            print('\033[34;1mVocê ainda é menor de idade, mas darei algumas informações: ')
            print('Falta \033[33;1;4m{} anos\033[34;1m para seu alistamento e será no ano de \033[33;1;4m{}\033[34;1m !!!'.format(falta,anoalistamento))
        else:
            print('\033[34;1mVocê ainda é menor de idade, mas darei algumas informações: ')
            print('Falta \033[33;1;4m{} ano\033[34;1m para seu alistamento e será no ano de \033[33;1;4m{}\033[34;1m !!!'.format(falta, anoalistamento))