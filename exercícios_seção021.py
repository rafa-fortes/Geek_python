

op = int(input(''' Digite uma das opções abaixo: \n
[1] Soma de 2 números.
[2] Diferença entre 2 números (maior pelo menor). 
[3] Produto entre 2 números.
[4] Divisão entre 2 números (o denominador não pode ser zero). 
Opção: '''))

if op == 1:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite um segundo número inteiro: '))
    print(f'A Soma é {n1 + n2}')

elif op == 2:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite um segundo número inteiro: '))
    if n1 < n2:
        print(f'A diferença é: {n2 - n1} ')
    else:
        print(f'A diferença é: {n1 - n2} ')

elif op == 3:
       n1 = int(input('Digite um número inteiro: '))
       n2 = int(input('Digite um segundo número inteiro: '))
       print(f'O valor do produto entre os números é: {n1*n2}')

elif op == 4:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite um segundo número inteiro: '))   
    if n1 > 0 or n2 > 0:
        print(f'A divisão entre esses números são: {n1 / n2} ')
    else:
        print('O denominador não pode ser zero ')      



