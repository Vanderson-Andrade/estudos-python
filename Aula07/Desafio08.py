'''
= = = = = Descrição = = = = =

Programa que ler uma media em metros e mostra ela em centimetros e em milimetros

'''
metros = float(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = centimetros * 10

print('+-+' * 10)
print('Metros = {} m\nCentimetros = {} cm\nMilimetros = {} mm'.format(metros, centimetros, milimetros))