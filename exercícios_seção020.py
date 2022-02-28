a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if a != b != c:
    print('Este triângulo é o Escaleno! ')
elif a == b == c:
    print('Este triângulo é o Equilátero! ')    
elif a == b != c:
    print('Este triângulo é o Isósceles! ')    