lista = {}
lista['aluno'] = str(input('Nome: '))
lista['média'] = float(input(f'Média de {lista["aluno"]}: '))
if lista['média'] > 7:
    lista['situação'] = 'aprovado'
elif lista['média'] < 7 and lista['média'] > 5:
    lista['situação'] = 'em recuperação'
else:
    lista['situação'] = 'reprovado'
print('-='*20)
for a, b in lista.items():
    print(f'{a} = {b}')
