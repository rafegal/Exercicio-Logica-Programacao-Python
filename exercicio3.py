lista = [1, 2, 10, 4, 1]

maior = 0

for i in lista:
    if maior == 0 or i > maior:
        maior = i

print(f'Maior valor da lista é {maior}')
