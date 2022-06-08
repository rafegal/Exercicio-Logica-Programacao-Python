turmas = int(input('Qual o total de turmas: '))

alunos = []

for i in range(turmas):
    alunos.append(int(input(f'Quantos alunos a turma {i} possui ?: ')))

    if alunos[i] < 0 or alunos[i] > 40:
        print('Informe um valor válido para a quantidade de alunos na turma!')

soma = sum(alunos)

med = soma / turmas

print(f'A média de alunos por turma é {med}')