num = int(input('Informe um número inteiro: '))

mult = 0

for i in range(2, num):
    if num % i == 0:
        mult = mult + i

if mult == 0:
    print('É primo!')
else:
    print('Não é primo!')
