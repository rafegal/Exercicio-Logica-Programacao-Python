print('<Espeecificaçaõ, Código, Preço>\n'
      'Cachorro Quente  100   R$ 1,20\n'
      'Bauru Simples  101  R$ 1,30\n'
      'Bauru com ovo  102  R$ 1,50\n'
      'Hambúrguer  103   R$ 1,20\n'
      'Cheeseburguer  104  R$ 1,30\n'
      'Refrigerante  105  R$ 1,00\n'
      'Quando o pedido estiver finalizado informe o número 0')

total = 0
soma = 0
while True:
    pedido = int(input('Informe o código do pedido: '))
    qt = int(input('Informe a quantidade desejada: '))

    if pedido == 100:
        total = qt * 1.20
        soma = total
        print(f'Total a se pagar pelo pedido de código 100: {total}')
    elif pedido == 101:
        total = qt * 1.30
        soma = soma + total
        print(f'\nTotal a se pagar pelo pedido de código 101: {total}')
    elif pedido == 102:
        total = qt * 1.50
        soma = soma + total
        print(f'\nTotal a se pagar pelo pedido de código 102: {total}')
    elif pedido == 103:
        total = qt * 1.20
        soma = soma + total
        print(f'\nTotal a se pagar pelo pedido de código 103: {total}')
    elif pedido == 104:
        total = qt * 1.30
        soma = soma + total
        print(f'\nTotal a se pagar pelo pedido de código 104: {total}')
    elif pedido == 105:
        total = qt * 1
        soma = soma + total
        print(f'\nTotal a se pagar pelo pedido de código 105: {total}')
    else:
        print('Informe um valor válido!')

    sn = input('Deseja pedir mais alguma coisa (s/n): ')

    if sn == 's':
        pass
    else:
        break



print(f'\n\nTotal a ser pago: {soma}')

