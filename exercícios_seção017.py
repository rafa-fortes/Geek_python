basemaior = float(input('Digite a base maior do trapézio: \n '))
basemenor = float(input('Digite a base menor: do trapézio: \n '))
altura = float(input('Digite a altura do trapézio: \n '))

area = (basemaior + basemenor) * altura

if basemaior <= 0 and basemenor <= 0:
    print('Número inválido! ')
else:
    print(f'A área do trapézio é: {area}')



