peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altua em metros:'))

def imc(peso, altura):
    print(peso / altura ** 2)

print('Seu IMC é:')
imc(peso, altura)


def hello(meu_nome):
    print('Olá', meu_nome)

hello('Dani')


def calcular_salario(qtd_horas_trabalhadas, valor_hora):
  if qtd_horas_trabalhadas <= 40:
    salario = (qtd_horas_trabalhadas*valor_hora)
  else:
    horas_excedidas = qtd_horas_trabalhadas - 40
    salario = 40 * valor_hora + (horas_excedidas * (1.5 * valor_hora))
  return salario

horas_trabalhadas = float(input('Digite as horas trabalhadas: '))
valor_hora = float(input('Digite o valor da hora: '))

salario_calculado = calcular_salario(horas_trabalhadas,valor_hora)
print('O valor do seu sálario é R$',salario_calculado)


'''
def calcular_pagamento(qtd_horas, valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas <= 40:
    salario=horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario

str_horas= input('Digite as horas: ')
str_taxa=input('Digite a taxa: ')
total_salario = calcular_pagamento(str_horas,str_taxa)
print('O valor de seus rendimentos é R$',total_salario)
'''


def calcular_salario(qtd_horas_trabalhadas, valor_hora):
  salario_sem_adicional = 0
  hora_extra_calculada = 0

  if qtd_horas_trabalhadas <= 40:
    horas_excedidas = 0
  else:
    horas_excedidas = qtd_horas_trabalhadas - 40  

  salario_sem_adicional = ((qtd_horas_trabalhadas - horas_excedidas)*valor_hora)
  hora_extra_calculada = (horas_excedidas * (1.5 * valor_hora))
  
  return salario_sem_adicional, hora_extra_calculada

horas_trabalhadas = float(input('Digite as horas trabalhadas: '))
valor_hora = float(input('Digite o valor da hora: '))

salario_sem_adicional, hora_extra_calculada = calcular_salario(horas_trabalhadas,valor_hora)

print('O valor do seu sálario base é R$',salario_sem_adicional)
print('Valor de horas excedidas de R$',hora_extra_calculada)

'''
O print também pode mostrar o resultado com o {} .format
'''