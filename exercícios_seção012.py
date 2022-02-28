from math import log 

n = int(input('Digite um número inteiro: '))

if n < 0:
    print('Número negativo ')

else:
    print(f'O algaritmo deste número é: {log(n)}')