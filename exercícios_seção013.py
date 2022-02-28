nota1 = float(input('Digite a primeira nota '))*1
nota2 = float(input('Digite a primeira nota '))*1
nota3 = float(input('Digite a primeira nota '))*2
media = (nota1 + nota2 + nota3) / 3
if media >= 60:
    print('Aluno aprovado! ')
else:
    print('Aluno reprovado! ')   
print(f'Sua média é: {media:.2f} ')     