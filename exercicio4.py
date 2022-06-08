lista = []

for i in range(0, 5):
    lista.append(float(input('Informe um valor: ')))

print(f'Lista = {lista}')

maior_num = 0

for i in lista:
    if maior_num == 0 or i > maior_num:
        maior_num = i

print(f'Maior valor da lista é {maior_num}')