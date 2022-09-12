item = []
mercado = []
while True:
    try:
        for i in range(1):
            item.append(input('Digite o nome do item: '))
            item.append(int(input('Digite a quantidade: ')))
            item.append(float(input('Digite o valor: R$ ')))
            mercado.append(item[:])
            item.clear()
    except ValueError:
        print('Entradas inválidas. Tente novamente.')
        continue
    
    while True:
        resposta = input('Deseja adicionar mais alguma coisa?\n 1 - Sim\n 2 - Não\nDigite a opção: ')
        if resposta != '1' and resposta != '2':
            print('Opção inválida.')
            continue
        else:
            break

    if resposta == '1':
        continue
    else:
        print('Cadastro realizado com sucesso. Itens adicionados:')
        break
for item in mercado:
    print('>> {}: R$ {}.' .format(item[0],item[2]))

print(mercado)