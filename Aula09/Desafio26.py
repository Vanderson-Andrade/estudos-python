'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Ler uma frase e mostra quantas vezes aparece a leta "a" em q possição ela aparece pela primeira vez e em que possição aparace pela ultima vez

'''
frase = str(input('Digite uma frase: '))
frase = frase.upper()

print('A letra "A" aparece : {} vezes nesta frase'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição {}'.format(frase.rfind('A')))
print('A letra "A" aparece a ultima vez na posição {}'.format(frase.rfind('A')))