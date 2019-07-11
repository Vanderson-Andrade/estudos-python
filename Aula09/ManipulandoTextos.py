'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição:

'''

'''
Fatiamento:
 
EX 1: frase = 'Curso em Vídeo'

frase[9] ==== permite pegar a letra que esta na pocisão 9 que no caso seria a letra "V"

frase[9:13] ==== permite pegar uma mini cadeia de caractere de acordo com o indicado

frase[9:21:2] ==== permite pegar uma mini cadeia de caractere pulando de 2 em 2

frase[:5] ==== permite pegar uma cadeia de caractere começando na possição "0" tambem poderia ser escrito "frase[0:5]"

frase[15:] ==== permite pegar uma cadeia de caractere a partir da possição informada ate o final da string

frase[9::3]====permite pegar uma mini cadeia de caractere aparte do numero informado ate o final da string pulando de 3 em 3

'''
'''
Análise:

len(frase) === mostra a quantidade de caractere ... incluindo espaços

frase.count('o') === conta quantas vezes existe a letra o na string  

frase.count('o', 0, 13) ==== conta quantas vezes aparece a letra o no intervalo das posições 0 e 13 

frase.find('deo') ==== mostro em que posição começa a palavra deo 

'Curso' in frase ==== diz em forma de valor boolean se tem a palavra Curso na string
'''
'''

Transformação: 

frase.replace('Python', 'Android') ==== permite fazer a troca da palavra Python para Android

frase.upper() ==== trasnforma todas as letras em maiusculas

frase.lower() ==== trasforma todas as letras em minusculas

fraser.captalize() ==== deixa a primeira letra maiuscula e todo o resto em minuscular ex: 'Curso em vídeo'

frase.title() ==== deixa a primeira letra de cada palavra em maiusculas ex: 'Curso Em Vídeo Python'

frase.strip() ==== faz a remoção de todos os espaços inuteis

frase.rstrip() ==== remove todos os espaços inuteis que estao a direita da string

frase.lstrip:() ==== remove todos os espaços inuteis que estao a esquerda  da string
'''
'''
Divisão:

frase.split() ==== Gera uma lista com todas as palavras de uma cadeia de caractere

'''
'''
Junção: 

' '.join(frase) ==== Junta todas a palavras em uma unica cadeia de caractere
'''
