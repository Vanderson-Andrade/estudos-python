'''
= = = = = Descrição = = = = =

Programa que ler um número e mostra seu dobro seu triplo e sua raiz quadrada

'''
num = float(input('Digite um valor: '))

d = num * 2
t = num * 3
rq = num ** (1/2)

print('=' * 20)

print('Número = {}\nSeu dobro = {}\nSeu triplo = {}\nSua raiz quadrada = {:.2f}'.format(num, d, t, rq))