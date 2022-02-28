print('=== Mini calculadora === ' )

print('''
[1] - adição 
[2] - subtração 
[3] - multiplicação
[4] - divisão 
''')
op = int(input('Escolha uma operação: '))

if op == 1:
    
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print(f'O resultado é: {n1 + n2} ')

elif op == 2:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número:'))
    print(f'O resultado é: {n1 - n2}')

elif op == 3:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print(f'O resultado é: {n1 * n2}')

elif op == 4:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print(f'O resultado {n1 / n2}')    