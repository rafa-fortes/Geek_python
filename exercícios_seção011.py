
n = int(input('Digite um número inteiro: '))
if n > 0: 
    a = int(n // 1 % 10 )
    b = int(n // 10 % 10)
    c = int(n // 100 % 10)
    d = int(n // 1000 % 10)

    soma = a + b + c + d

    print(f'A soma dos algorismo é {soma}')
else:
    print('Número invalido ')    


    