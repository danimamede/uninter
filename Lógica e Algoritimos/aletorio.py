peca = []
cadastrados = []

# ---- CADASTRO DE PEÇAS
def cadastrarPeca(codigoPeca):
    print('\nCADASTRO DE PEÇAS')
    peca = []
    cadastrados = []
    while True:
        try:
            peca.append(input('Digite o nome do peça: '))
            peca.append(input('Digite o nome do fabricante: '))
            peca.append(float(input('Digite o valor: R$ ')))
            cadastrados.append(peca[:])
            peca.clear()
        except ValueError:
            print('Entradas inválidas. Tente novamente.')
            continue
    
        while True:
            resposta = input('Deseja adicionar mais alguma coisa?\n 1 - Sim\n 2 - Não\n >> ')
            if resposta != '1' and resposta != '2':
                print('Opção inválida.')
                continue
            else:
                break

        if resposta == '1':
            continue
        else:
            print('Cadastro realizado com sucesso.\nRetornando ao menu.\n')
            break

# --- CONSULTA PEÇAS
def consultaPeca():
    print('\nCONSULTA DE PEÇAS')

# ----- REMOVER PEÇAS
def removerPeca():
    print('\nREMOÇÃO DE PEÇAS')

# ----- MAIN
print('Bem vindo(a) ao Controle de Estoque da Bicicletaria Daniela Mamede.')
codigoPeca = 000
while True:
    print('------ MENU ------\n1- Cadastrar peças\n2- Consultar peças\n3- Remover peças\n4- Sair')
    opcao = input('Escolha a opção desejada: ')
    if opcao == '1':
        codigoPeca = codigoPeca + 1
        cadastrarPeca(codigoPeca)
    elif opcao == '2':
        consultaPeca()
    elif opcao == '3':
        removerPeca()
    elif opcao == '4':
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida. Tente novamente.\n')
        continue