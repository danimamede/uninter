# FUNÇÃO DIMENSÕES DO OBJETO
def dimensoesObjeto():
    while True:
        try:
            altura = float(input('Digite a altura do objeto (em cm): '))
            lagura = float(input('Digite a largura do objeto (em cm): '))
            comprimento = float(input('Digite o comprimento do objeto (em cm): '))
            volume = altura * lagura * comprimento
            print('O volume do objeto (em cm³) é: {}\n' .format(volume))
            if volume >= 0.1 and volume <= 1000:
                return 10
            elif volume >= 1001 and volume <= 10000:
                return 20
            elif volume >= 10001 and volume <= 30000:
                return 30
            elif volume >= 30001 and volume <= 100000:
                return 50
            else:
                print('Objeto com dimensões erradas ou acima do máximo permitido (até 100000cm³).')
                print('Insira os valores novamente.')
                continue
        except ValueError:
            print('Por favor digite valores numéricos.')
            continue

# FUNÇÃO PESO DO OBJETO
def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg): '))
            if peso >= 0.0 and peso <=0.1:
                return 1
            elif peso >= 0.11 and peso <= 1:
                return 1.5
            elif peso >= 1.10 and peso <= 10:
                return 2
            elif peso >= 10.1 and peso <= 30:
                return 3
            else:
                print('Objeto com peso errado ou acima do máximo permitido (até 30kg).')
                print('Insira os valores novamente.')
                continue
        except ValueError:
            print('Por favor digite valores numéricos.')
   
# FUNÇÃO ROTA DO OBJETO
def rotaObjeto():
    print('\nRotas disponíveis:\nBR - Brasília para Rio de Janeiro\nBS - Brasília para São Paulo\nRB - Rio de Janeiro para Brasília\nRS - Rio de Janeiro para São Paulo\nSR - São Paulo para Rio de Janeiro\nSB - São Paulo para Brasília\n')
    while True:
        rota = input('Digite a rota que deseja: ')
        if rota == 'BR':
            return 1.5
        if rota == 'BS':
            return 1.2
        if rota == 'RB':
            return 1.5
        if rota == 'RS':
            return 1
        if rota == 'SR':
            return 1
        if rota == 'SB':
            return 1.2
        else:
            print('Você digitou uma rota inválida.')
            print('Tente novamente utilizando uma das siglas informadas na tabela acima.\n')
            continue

# MAIN
def main():
    print('Bem vindo(a) à Companhia de Logística Daniela Mamede\n')
    dimensoes = dimensoesObjeto()
    peso = pesoObjeto()
    rota = rotaObjeto()
    total = (dimensoes * peso * rota) 
    print('O valor total a pagar é de: R$ {:.2f}' .format(total))

while True:
    entrada = input('Deseja inserir um produto para cálculo?\n1 - SIM\n2 - NÃO\n')
    if (entrada == '1'):
        main()
    else:
        break
    