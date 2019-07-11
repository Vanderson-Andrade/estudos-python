'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição:

'''

'''
simples:

if condição:
    bloco verdadeiro
else:
    bloco falso
    
simples(simplificada)
'bloco verdadeiro' if condição else 'bloco falso'

'''
#Exemplos:

tempo = int(input('Quantos anos tem seu carro: '))
if tempo <= 3 :
    print('Carro Novo')
else:
    print('Carro Velho')

print('Carro Novo'if tempo <= 3 else 'Carro Velho')