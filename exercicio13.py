print('1 - João\n'
      '2 - Marcos\n'
      '3 - Regina\n'
      '4 - Adeilson')

eleitores = int(input('Insira o total de eleitores: '))

cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco = 0

for votos in range(eleitores):
    escolha = int(input('Informe seu voto: '))
    if escolha == 1:
        cand1 = cand1 + 1
    elif escolha == 2:
        cand2 = cand2 + 1
    elif escolha == 3:
        cand3 = cand3 + 1
    elif escolha == 4:
        cand4 = cand4 + 1
    elif escolha == 5:
        nulo = nulo + 1
    elif escolha == 6:
        branco = branco + 1
    else:
        print('Informe um valor válido!')

perc_nulo = (nulo * 100) / eleitores
perc_branco = (branco * 100) / eleitores

print(f'João obteve {cand1} votos\n'
        f'Marcos obteve {cand2} votos\n'
        f'Regina obteve {cand3} votos\n'
        f'Adeilson obteve {cand4} votos\n\n'
        f'Total de votos nulos: {nulo}\n'
        f'Total de votos em branco {branco}\n\n'
        f'Percentual dos votos nulos foi de {perc_nulo}%, e dos votos em branco {perc_branco}%')


