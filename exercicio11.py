inter1 = 0
inter2 = 0
inter3 = 0
inter4 = 0

while True:
    n = int(input('Digite um número: '))

    if n >= 0 or n <= 25:
        inter1 = inter1 + 1
    elif n >= 26 or n <= 50:
        inter2 = inter2 + 1
    elif n >= 51 or n <= 75:
        inter3 = inter3 + 1
    elif n >= 76 or n <= 100:
        inter4 = inter4 + 1
    elif n == 0:
        break

print(f'{inter1} números entre 0 e 25\n'
      f'{inter2} números entre 26 e 50\n'
      f'{inter3} números entre 51 e 45\n'
      f'{inter4} números entre 76 e 100')