print('Bem vindo(a) à Loja Vitual Dokas')
valor_produto = float(input('Informe o valor do produto: R$ '))
qtd = int(input('Informe a quantidade que deseja adquirir: '))

if valor_produto <= 0 or qtd <= 0:
    print('Entradas inválidas')
else:
    if qtd <= 9:
        desconto = 0
    elif (qtd >= 10 and qtd <= 99):
        desconto = (valor_produto * qtd) * 0.05
    elif (qtd >= 100 and qtd <=999):
        desconto = (valor_produto * qtd) * 0.1
    else:
        desconto = (valor_produto * qtd) * 0.15

print('O valor da compra sem desconto é de: R$ {:.2f}' .format(valor_produto * qtd))
print('O valor de desconto aplicado nessa compra é de: R$ {:.2f}' .format(desconto))
print('O valor total da sua compra é de: R$ {:.2f}' .format((valor_produto * qtd) - desconto))