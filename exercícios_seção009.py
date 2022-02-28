salario = float(input('Digite o valor do salário: '))
prestacao = float(input('Digite o valor da prestação: '))

limite = (salario * 20) / 100

if prestacao <= limite:

    print('Empréstimo concedido ')

else:

    print('Empréstimo não concedido ')

