'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: se é posivel forma um trianguloe de que tipo

'''

print('\033[36;1m*=\033[m'*20)
titulo = ' Análise de Triângulos '
print('\033[33m{:*^40}'.format(titulo))
print('\033[36;1m*=\033[m'*20)

a = float(input('Digite o segmento "A": '))
b = float(input('Digite o segmento "B": '))
c = float(input('Digite o segmento "c": '))

if a < b+c and b < c+a and c < a+b:
    print('Os segmentos podem formar um triângulo do tipo: ')

    if a == b and a == c:
        print('equilatero')
    elif a == b or a == c or b == c:
        print('isósceles')
    elif a != b and a != c and b != c:
        print('escaleno')
else:
    print('Nada de triangulo')