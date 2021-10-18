from datetime import date #importando calendário
maior = 0
menor = 0
for idade in range(1, 8):
    data = int(input('Digite a data de nascimento da {}ª pessoa: '.format(idade)))
    if date.today().year - data < 18: #usando ano do calendário
        menor += 1
    else:
        maior += 1
print('Tivemos um total de {} pessoas menores de idade, e {} maiores de idade'.format(menor, maior))
