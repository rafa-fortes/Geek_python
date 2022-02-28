nota1lab = float(input('Digite a nota do laboratório: '))*2
nota2av = float(input('Digite a nota da avaliação semestral: '))*3
nota3final = float(input('Digite o valor do exame final: '))*5

media = (nota1lab + nota2av + nota3final) / 10
    
if media >= 0 and media <= 2.9:
    print('Você foi reprovado!! ')

elif media >= 3 and media <= 4.9:
    print('Você ficou de recuperação! ')

elif media >= 5 and media <= 10:
    print('Você foi aprovado! ')
else:
    print('Nota invalida! Informar notas entre 0 até 10 ')  
  
