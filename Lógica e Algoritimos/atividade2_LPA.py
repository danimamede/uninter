print('Bem vindo(a) à Lanchonete da Daniela Mamede')
print('*****************    CARDÁPIO    *****************')
print('|  CÓDIGO  |         PRODUTO         |   VALOR   |')
print('|   100    |    Cachorro Quente      |    9,00   |')
print('|   101    |  Cachorro Quente Duplo  |   11,00   |')
print('|   102    |         X-Egg           |   12,00   |')
print('|   103    |        X-Salada         |   12,00   |')
print('|   104    |         X-Bacon         |   14,00   |')
print('|   105    |         X-Tudo          |   17,00   |')
print('|   200    |    Refrigerante Lata    |    5,00   |')
print('|   201    |       Chá Gelado        |    4,00   |')
acumulador = 0

# Inicio das entradas do pedido com estrutura de repetição caso queira mais de um produto
while True:
    codigo = input('Digite o código do produto: ')
    if codigo == '100':
        print('Cachorro Quente adicionado ao seu pedido.')
        acumulador = acumulador + 9.00
    elif codigo == '101':
        print('Cachorro Quente Duplo adicionado ao seu pedido.')
        acumulador = acumulador + 11.00
    elif codigo == '102':
        print('X-Egg adicionado ao seu pedido.')
        acumulador = acumulador + 12.00
    elif codigo == '103':
        print('X-Salada adicionado ao seu pedido.')
        acumulador = acumulador + 12.00
    elif codigo == '104':
        print('X-Bacon adicionado ao seu pedido.')
        acumulador = acumulador + 14.00
    elif codigo == '105':
        print('X-Tudo adicionado ao seu pedido.')
        acumulador = acumulador + 17.00
    elif codigo == '200':
        print('Refrigerante Lata adicionado ao seu pedido.')
        acumulador = acumulador + 5.00
    elif codigo == '201':
        print('Chá Gelado adicionado ao seu pedido.')
        acumulador = acumulador + 4.00
    else:
        print('Código inválido.')
        continue

# Estrutura de repetiçao aninhada caso a entrada digitada seja inválida
    while True:
        resposta = input('Deseja adicionar mais alguma coisa?\n Sim = 1\n Não = 2\n Insira a opoção desejada:')
        if resposta != '1' and resposta != '2':
            print('Opção inválida.')
            continue
        else:
            break

    if resposta == '1':
        continue
    else:
        print('O valor total do seu pedido é de R$ {:.2f}' .format(acumulador))
        break