# Exercício utilizando 2 estruturas de repetição aninhadas. 2 WHILE

'''
tabuada = 1
while tabuada <= 10:
    print('TABUADA DO {}: ' .format(tabuada))
    i = 1
    while i <=10:
        print('{} x {} = {}' .format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1
'''

# Exercício utilizando 2 FOR

for tabuada in range (1, 11, 1):
    print('TABUADA DO {}' .format(tabuada))
    for i in range (1, 11, 1):
        print('{} x {} = {}' .format(tabuada, i, tabuada * i))


# Exercício utilizando 1 WHILE e 1 FOR (também pode ser o contrário)