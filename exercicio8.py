eleitores = int(input('Quanatidade de eleitores: '))

candidato13 = 0
candidato17 = 0
candidato25 = 0

for i in range(1, eleitores):
    voto = int(input('Em quem deseja votar ?: '))

    if voto == 13:
        candidato13 = candidato13 + 1
    elif voto == 17:
        candidato17 = candidato17 + 1
    elif voto == 25:
        candidato25 = candidato25 + 1
    else:
        print('Informe um número de votação válido!')

print(f'13 - Rafael: {candidato17}\n17 - Felipe: {candidato17}\n25 - Galleani: {candidato25}')