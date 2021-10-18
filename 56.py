nomevelho = ''
media = 0
velho = 0
mulheres = 0
for dados in range(1, 5):
    print('----- {}ª PESSOA -----'.format(dados))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    media += idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome
print('A média de idade do grupo é de {} anos.'.format(media / 4))
print('O homem mais velho é o {} com {} anos.'.format(nomevelho, velho))
print('Ao todo são {} mulhere(s) com menos de 20 anos'.format(mulheres))


