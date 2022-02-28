import math

num_r = float(input('Digite um número real: '))
if num_r >= 0:
    print(f'A raiz quadrada do número real é: {math.sqrt(num_r)} ')
else:
    print(f'O número ao quadrado é: {num_r ** 2} ')
