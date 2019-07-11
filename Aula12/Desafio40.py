'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: media escolar

'''
nome = str(input('Aluno: '))
nome = nome.upper().split()
nota = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota + nota2) / 2.0

print('-='*20)
print('''          TABELA DE APROVAÇÃO
----------------------------------------
\033[32;4mAPROVADO\033[m = MÉDIA MAIOR OU IGUAL A 7.0
\033[33;4mRECUPERAÇÃO\033[m = MÉDIA ENTRE 5.0 E 6.9
\033[31;4mREPROVADO\033[m = MÉDIA ABAIXO DE 5.0''')
print('-='*20)

if (nota < 0 or nota2 < 0 ) or (nota > 10 or nota2 > 10 ):
    print('\033[31;1;4mVALOR DE NOTA INVÁLIDO !')

elif media < 5:
    print('\033[31;4m{}\033[m não obteve nota suficiente para uma aprovação.\nMédia: \033[31;4m{:.1f}\033[m.\nSituação: \033[31;4mREPROVADO!'.format(nome[0], media))

elif media >= 5 and media <= 6.9:
    print('\033[33;4m{}\033[m não obteve nota suficiente para uma aprovação.\nMédia: \033[33;4m{:.1f}\033[m.\nSituação: \033[33;4mRECUPERAÇÃO!'.format(nome[0], media))

else:
    print(
        '\033[32;4m{}\033[m parabéns você obteve nota suficiente para uma aprovação.\nMédia: \033[32;4m{:.1f}\033[m.\nSituação: \033[32;4mAPROVADO!'.format(
            nome[0], media))