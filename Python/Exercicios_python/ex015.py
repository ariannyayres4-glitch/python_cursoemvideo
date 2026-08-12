from random import choice
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
sala = [al1, al2, al3, al4]
print(f'O aluno(a) escolido foi {choice(sala)}')