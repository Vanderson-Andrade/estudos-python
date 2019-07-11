'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: recebe um ano e diz se é bissexto ou não

'''
from datetime import date
ano = int(input('Qual o ano que você quer analisar? Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))