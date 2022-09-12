'''
Condicional SIMPLES: um bloco de ações é executado se for verdadeiro
ou então nada acontece e pula a etada de instruções
'''


x = int(input('Digite um valor inteiro:'))
y = int(input('Digite um segundo valor inteiro:'))

if(x > y):
    print('O primeiro valor é maior do que o segundo!')


'''
Condicional COMPOSTA: um bloco de ações para uma tomada de decisões
e outro bloco de instruções (else) para outra tomada de decisões
'''


x = int(input('Digite um valor inteiro:'))
y = int(input('Digite um segundo valor inteiro:'))

if(x > y):
    print('O primeiro valor é maior do que o segundo!')

else:
    print('O segundo valor é maior do que o primeiro!')



a = int(input('Digite um número inteiro:'))
if(a % 2 == 0):
    print(a, 'é um número par!')

else:
    print(a, 'é um número impar!')

'''
Expressões lógicas not, and e or
'''

m1 = float(input('Digite a nota de matemática:'))
m2 = float(input('Digite a nota de português:'))
m3 = float(input('Digite a nota de inglês:'))

if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('O aluno passou de ano!')
else:
    print('O aluno não passou de ano.')


'''
Condicionais ANINHADAS
'''

print('Olá. Estes são os produtos disponíveis:')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Digite o número do produto que deseja comprar:'))
qtd = int(input('Quantas unidades deseja comprar?'))

if(produto == 1):
    pagar = qtd * 3.60
    print('Você comprou {} maçãs. Total à pagar: R${}' .format (qtd, pagar))

else:
    if(produto == 2):
        pagar = qtd * 3.60
        print('Você comprou {} laranjas. Total à pagar: R${}' .format(qtd, pagar))

    else:
        if(produto == 3):
            pagar = qtd * 1.85
            print('Você comprou {} bananas. Total à pagar: R$ {}' .format(qtd, pagar))
        else:
            print('Produto inexistente.')



print('Olá. Estes são os produtos disponíveis:')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Digite o número do produto que deseja comprar:'))
qtd = int(input('Quantas unidades deseja comprar?'))

if(produto == 1):
    pagar = qtd * 3.60
    print('Você comprou {} maçãs. Total à pagar: R${}' .format (qtd, pagar))

elif(produto == 2):
    pagar = qtd * 3.60
    print('Você comprou {} laranjas. Total à pagar: R${}' .format(qtd, pagar))

elif(produto == 3):
    pagar = qtd * 1.85
    print('Você comprou {} bananas. Total à pagar: R$ {}' .format(qtd, pagar))
        
else:
    print('Produto inexistente.')
