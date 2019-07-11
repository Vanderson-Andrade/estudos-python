'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição:

'''

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:12])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
frase = '    Curso em Vídeo Python   '
print(len(frase))
print(len(frase.strip()))
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Aandroid'))
print(frase)
frase = frase.replace('Python', 'Aandroid')
print(frase)
frase = frase.replace('Aandroid', 'Python')
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

