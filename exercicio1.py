while True:
    nome = str(input('Informe seu nome de usuário: '))
    senha = str(input('Informe sua senha: '))

    if nome == senha:
        print('O nome de usuário não pode ser igual a senha!')
    else:
        print('Tudo certo!')
