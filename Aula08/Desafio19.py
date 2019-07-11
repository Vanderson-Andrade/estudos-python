import random

aluno1 = input('Digite o primeiro aluno:')
aluno2 = input('Digite o segundo aluno:')
aluno3 = input('Digite o terceiro aluno:')
aluno4 = input('Digite o quato aluno:')

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(alunos)

print('Aluno escolhido : {:*^20}'.format(sorteado))