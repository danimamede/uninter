'''
peso = float(input('Digite o seu peso:'))
altura = float(input('Digite sua altura em metros:'))

imc = peso / (altura **2)
print('O seu IMC é: {}' .format(imc))

if imc > 30:
    print('Seu IMC é indicativo de obesidade')

else:
    print('Seu IMC não é indicativo de obesidade')
'''

#Função sem definição de variáveis dentro da função
def IMC():
    altura =  float(input('Digite sua altura (m): '))
    peso = float(input('Digite seu peso (kg): '))
    imc = peso / altura ** 2
    print('Seu IMC é: {:.2f}' .format(imc))
    if imc > 30:
        print('Indicativo de obesidade.')
    else:
        print('Não é indicativo de obesidade.')

IMC()

#Função com definição de variáveis dentro da função
def IMC(a, p):
    altura =  float(input(a))
    peso = float(input(p))
    imc = peso / altura ** 2
    print('Seu IMC é: {:.2f}' .format(imc))
    if imc > 30:
        print('Indicativo de obesidade.')
    else:
        print('Não é indicativo de obesidade.')

IMC('Digite sua altura(m): ', 'Digite o seu peso(kg): ')




# Função sem definição de parâmetros
def IMC():
    altura =  float(input('Digite sua altura (m): '))
    peso = float(input('Digite seu peso (kg): '))
    imc = peso / altura ** 2
    print('Seu IMC é: {:.2f}' .format(imc))
    if imc > 30:
        print('Indicativo de obesidade.')
    else:
        print('Não é indicativo de obesidade.')

IMC()

# Função com definição de parâmetros.
def borda(s1):
    tam = len(s1)
    if tam:
        print('+','-' * tam,'+')
        print('|', s1, '|')
        print('+','-' * tam,'+')

borda('Olá!')
borda('Prazer, meu nome é Dani')  