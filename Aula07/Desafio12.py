'''
= = = = = Descrição = = = = =

Programa que ler o preço de um produto e mostra seu novo preço com desconto

'''
preco = float(input('Digite o preço do produto: '))

novoPreco = preco - (preco * 0.05)

print('Preço com desconto: R$ {}'.format(novoPreco))