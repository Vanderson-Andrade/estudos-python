'''
= = = = = Descrição = = = = =

Programa que ler duas notas de um aluno e faz o calculo de sua média

'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite uma segunda nota: '))
media = (nota1 + nota2) / 2
print('*'*20)

print('Média: {}'.format(media))