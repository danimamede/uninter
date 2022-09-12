preco = float(input('Digite o preco do produto:'))
p = float(input('Digite o percentual de desconto'))

desconto = preco * (p / 100)
preco_final = preco - desconto

print('O preço do produto é R${}. O valor do desconto é de {}%'.format(preco, p))
print('O desconto é R${}. O preço final do produto é de R${}' .format(desconto, preco_final))


quantidade_km = int(input('Digite quanto quilômetros foram percorridos:'))
quantidade_dias = int(input('Digite quantos dias o carro foi alugado:'))

preco_total = (60 * quantidade_dias) + (0.15 * quantidade_km)

print('Quilometragem percorrida: {}. Dias de aluguel: {}' .format(quantidade_km, quantidade_dias))
print('O valor total a ser pago é de R${}' .format(preco_total))


frase = input('Digite uma frase:')
tam = len(frase)

frase2 = frase[:int(tam/2)]
print(frase2[-2:])
