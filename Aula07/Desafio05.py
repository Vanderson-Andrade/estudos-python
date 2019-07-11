'''
= = = = = Descrição = = = = =

Programa que ler um número e mostra seu sucessor e seu antecessor

'''

num = int(input('Digite um número: '))

inc = num+1
dec = num-1
print('='*20)
print('Sucessor = {0}\nAntecessor = {1}'.format(inc, dec))