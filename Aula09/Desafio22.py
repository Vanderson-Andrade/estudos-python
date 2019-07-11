'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Ler o nome completo de uma pessoa e mostra o nome com todas as letras em maiusculas, todas as letras minusculas, quantas letras ao todo sem considerar espaços, quantas letras tem o primeiro nome

'''
nome = str(input('Digite seu nome completo: '))
print(nome.upper())#Mostra o nome em maiusculas
print(nome.lower())#Mostra o nome em minusculas

nome = nome.split()#Divide o nome em lista
print(len(''.join(nome)))#Faz a junção das palavras sem espaços e conta quantas letras tem
print(len(nome[0]))#Mostra quantas letras tem o primeiro nome