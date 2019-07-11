'''
+ => Adição
- => Subtração
* => Multiplicação
/ => Divisão
** pow(numero base, numero da potência) => Potência
**(1/2) => Raiz quadrada
// => Divisão Inteira
% => Resto da Divisão (Modulo)

= = = = = ORDEM DE PRECEDÊNCIA = = = = =

1º Ordem == ()
2º Ordem == **
3º Ordem == * /, //, %
4º Ordem == + -

= = = = = Alinhamento de texto = = = = =

< => alinhamento a esquerda
> => alinhamento a direita
^ => alinhamento centralizado

Ex: print('Prazer em te conhecer {:=^20}'.format(variavel), end=' ' <- faz com que não aja uma quebra de linha)
Ex2: print('A soma vale {}, \n"Faz com que aja uma quebra de linha" o produto vale {}, e a divisão é {:.3f"<- estou formatando a quantidade de casas decimais"} '.format(soma, multiplicação, divisão)

onde estar o numero 20 define a quantidade de espaço em caractere que uma palavra irar ocupar.

Se colocar um caractere entre o ponto duplo e o alinhamento você define um caractere para ocupar os espaços que ficaram vazios

'''

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro número: '))

som = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
divi = n1 // n2
res = n1 % n2

print('Adição = {}'.format(som))
print('Subtração = {}'.format(sub))
print('Multiplicação = {}'.format(mult))
print('Divisão = {}'.format(div))
print('Potênciação = {}'.format(pot))
print('Divisão Inteira = {}'.format(divi))
print('Resto da Divisão = {}'.format(res))
