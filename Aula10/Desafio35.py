'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: ler tres segmentos e dizer se é posivel forma um triangulo

'''
print('\033[32;1m-=\033[m'*13)
print('   \033[36;1mDesafio do Triangulo\033[m   ')
print('\033[32;1m-=\033[m'*13)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2 :
    print('\033[32;1m\nOs segmentos podem formar um triângulo\033[m')
else:
    print('\033[31;1m\nOs segmentos não podem formar um triângulo\033[m')
