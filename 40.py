nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Reprovado')
elif media >= 5 and media < 7:
    print('Recuperação')
else:
    print('Aprovado')
print('Sua média foi {:.1f}'.format(media))