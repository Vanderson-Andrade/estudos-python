'''
= = = = = Descrição = = = = =

Programa que ler altura e largura de uma parede, mostra sua area e quanto de tinta é nescesario para pintar essa parede

Obs: 1L de tinta = 2m² de parede pintada

'''

base = float(input('Digite a largura da parede: '))
altura = float(input('Agora digite a altura: '))

area = base * altura
tinta = area / 2

print('Área = {} m²'.format(area))
print('Será nescesario {}l de tinta para pintar {}m²'.format(tinta, area))