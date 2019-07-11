'''
@autor: Vanderson Andrade
@data: 00/00/2019
@versão: 1.0
@descrição: Ler no nome de uma cidade e diz se ela começa com o nome SANTO

'''
cidade = str(input('Digite o nome de uma Cidade: '))
cidade = cidade.upper()
print('Essa cidade começa com o nome "Santo": {}'.format('SANTO' in cidade[0:5]))