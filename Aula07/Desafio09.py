'''
= = = = = Descrição = = = = =

Programa que ler um número e mostra sua tabuada de adição subtração multiplicação e divisão

'''
print('= = = = = TABUADA = = = = =')

numero = float(input('Digite um valor inteiro: '))

calc0 = numero + 0
calc1 = numero + 1
calc2 = numero + 2
calc3 = numero + 3
calc4 = numero + 4
calc5 = numero + 5
calc6 = numero + 6
calc7 = numero + 7
calc8 = numero + 8
calc9 = numero + 9
calc10 = numero + 10

print('**********')
print('= ADIÇÂO =\n\n01 + {0} = {2}\n02 + {0} = {3}\n03 + {0} = {4}\n04 + {0} = {5}\n05 + {0} = {6}\n06 + {0} = {7}\n07 + {0} = {8}\n08 + {0} = {9}\n09 + {0} = {10}\n10 + {0} = {11}\n\n'.format(numero, calc0, calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8, calc9, calc10),)


calc1 = numero - 1
calc2 = numero - 2
calc3 = numero - 3
calc4 = numero - 4
calc5 = numero - 5
calc6 = numero - 6
calc7 = numero - 7
calc8 = numero - 8
calc9 = numero - 9
calc10 = numero - 10


print('= SUBTRAÇÃO =\n\n\n01 - {0} = {1}\n02 - {0} = {2}\n03 - {0} = {3}\n04 - {0} = {4}\n05 - {0} = {5}\n06 - {0} = {6}\n07 - {0} = {7}\n08 - {0} = {8}\n09 - {0} = {9}\n10 - {0} = {10}'.format(numero, calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8, calc9, calc10))


calc0 = numero * 0
calc1 = numero * 1
calc2 = numero * 2
calc3 = numero * 3
calc4 = numero * 4
calc5 = numero * 5
calc6 = numero * 6
calc7 = numero * 7
calc8 = numero * 8
calc9 = numero * 9
calc10 = numero * 10

print('= Multiplicação =\n\n00 * {0} = {1}\n01 * {0} = {2}\n02 * {0} = {3}\n03 * {0} = {4}\n04 * {0} = {5}\n05 * {0} = {6}\n06 * {0} = {7}\n07 * {0} = {8}\n08 * {0} = {9}\n09 * {0} = {10}\n10 * {0} = {11}'.format(numero, calc0, calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8, calc9, calc10))



calc1 = numero / 1
calc2 = numero / 2
calc3 = numero / 3
calc4 = numero / 4
calc5 = numero / 5
calc6 = numero / 6
calc7 = numero / 7
calc8 = numero / 8
calc9 = numero / 9
calc10 = numero / 10

print('= DIVISÃO =\n\n\n01 / {0} = {1}\n02 / {0} = {2}\n03 / {0} = {3}\n04 / {0} = {4}\n05 / {0} = {5}\n06 / {0} = {6}\n07 / {0} = {7}\n08 / {0} = {8}\n09 / {0} = {9}\n10 / {0} = {10}'.format(numero, calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8, calc9, calc10))