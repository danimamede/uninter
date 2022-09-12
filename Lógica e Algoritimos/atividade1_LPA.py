print('Bem vindo(a) à Loja da Daniela Mamede')
valor_produto = float(input('Informe o valor unitário do produto: R$ '))
qtd = int(input('Informe a quantidade: '))
porcentagem_desconto = 0

# Estrutura de repetição para auxiliar o usuário a inserir números positivos e maiores do que zero
while (valor_produto <= 0 or qtd <= 0):
    print('Entradas inválidas. Insira valores maiores do que 0.')
    valor_produto = float(input('Informe o valor do produto: R$ '))
    qtd = int(input('Informe a quantidade que deseja adquirir: '))

# Condicionais para aplicação de desconto com base na quantidade de produtos adquiridos
if (qtd >= 1 and qtd <= 9):
    desconto = 0
elif (qtd >= 10 and qtd <= 99):
    desconto = (valor_produto * qtd) * 0.05
    porcentagem_desconto = 5
elif (qtd >= 100 and qtd <=999):
    desconto = (valor_produto * qtd) * 0.1
    porcentagem_desconto = 10
else:
    desconto = (valor_produto * qtd) * 0.15
    porcentagem_desconto = 15

# Retorno para o usuário com base nas entradas informadas.
# Demonstrativo de valor sem desconto, percentual e valor do desconto e total final após desconto aplicado
print('O valor da compra sem desconto é de: R$ {:.2f}' .format(valor_produto * qtd))
print('O valor de desconto é de {}% (R$ {:.2f})' .format(porcentagem_desconto, desconto))
print('O valor total da sua compra é de: R$ {:.2f}' .format((valor_produto * qtd) - desconto))