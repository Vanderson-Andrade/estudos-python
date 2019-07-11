'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: dizer a categoria do nadador

'''
from datetime import  date

nascimento = int(input('Nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento

if idade <= 9.0:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade > 19 and idade <= 20:
    print('Sênior')
elif idade > 20:
    print('Master')