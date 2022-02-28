sexo = (input('Informe seu sexo (m/f): '))
altura = float(input('Digite sua altura: '))

m = (72.7 * altura) - 58
f = (62.1 * altura) - 44.7

if sexo != 'm' and sexo != 'f':
    print('Sexo invalido! ')

elif sexo == 'm':    
    print(f'Seu peso ideal é: {m:.2f} ')

else:
    print(f'Seu peso ideal é: {f:.2f} ')  
      

