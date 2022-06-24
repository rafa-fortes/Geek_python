idade = int(input('Digite a sua idade: '))
tempo = int(input('Digite o tempo de serviço:  '))

if idade >= 65:
    print('Apto para aposentadoria ')

elif tempo >= 30:
    print('Apto para aposentadoria ')  

elif idade >= 60 and tempo >= 25:
    print('Apto para aposentadoria ')
    
else: 
    print('Não apto para aposentadoria ')              
