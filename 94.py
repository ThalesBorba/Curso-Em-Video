cadastro = {}
nome = []
sexo = []
idade = []
mulheres = []
c = 0
idadetotal = 0
while True:
    nome.append(str(input('Nome: ')))
    sexo.append(str(input('Sexo: [M/F] ')))
    while sexo[c] not in 'MF':
        sexo.pop()
        sexo.append(str(input('Erro! Escolha M ou F: ')))
    idade.append(int(input('Idade: ')))
    c += 1
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print('-='*20)
print(f'Ao todo temos {len(nome)} pessoas cadastradas')
for c in range(0, len(idade)):
    idadetotal += idade[c]
print(f'A média total de idade é de {idadetotal / len(idade):.0f}')
print('As mulheres cadastradas foram: ')
for c in range(0, len(sexo)):
    if sexo[c] == 'F':
        mulheres = nome[c]
        print(f'{mulheres} ', end='')
print('Lista das pessoas com a idade acima da média:')
for c in range(0, len(idade)):
    if idade[c] > idadetotal / len(idade):
        cadastro['nome'] = nome[c]
        cadastro['sexo'] = sexo[c]
        cadastro['idade'] = idade[c]
        for a, b in cadastro.items():
            print(f'{a} = {b}; ', end='')
        print()

