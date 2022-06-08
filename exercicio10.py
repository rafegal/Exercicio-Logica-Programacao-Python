maior_altura = 0
menor_altura = 200
h_aluno = 0
s_aluno = 0

for i in range(1, 11):
    altura = int(input(f"Informe a altura do aluno {i} em cm: "))

    if altura > maior_altura:
        h_aluno = i
        maior_altura = altura
    if altura < menor_altura:
        s_aluno = i
        menor_altura = altura

print(f"Número do aluno mais alto e sua altura: {h_aluno} , {maior_altura}cm"
      f"\nNúmero do aluno mais baixo e sual altura: {s_aluno} com {menor_altura}cm")



