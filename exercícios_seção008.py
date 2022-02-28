nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

passou = True

if nota1 > 10 or nota2 > 10:
    passou = False
    print('Nota invalida! ')

if nota1 < 0 or nota2 < 0:
    passou = False
    print('Nota invalida!')

if passou:
    media = (nota1 + nota2) / 2
    print(f'A média das notas {nota1} e {nota2} é {media}')
