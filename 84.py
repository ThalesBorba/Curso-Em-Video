list = []
deflist = []
maior = menor = 0
while True:
    list.append(str(input('Nome: ')))
    list.append(float(input('Peso: ')))
    if len(deflist) == 0:
        maior = menor = list[1]
    else:
        if list[1] > maior:
            maior = list[1]
        if list[1] < menor:
            menor = list[1]
    deflist.append(list[:])
    list.clear()
    escolha = str(input('Deseja continuar? [S/N): ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N): ')).upper().strip()[0]
    if escolha == 'N':
        break
print()
print(f'Você cadastrou {len(deflist)} pessoas')
print(f'O maior peso foi de {maior}kgs, de ', end='')
for c in deflist:
    if maior == c[1]:
        print(c[0], end=' ')
print()
print(f'O menor peso foi de {menor}kgs, de ', end='')
for c in deflist:
    if c[1] == menor:
        print(c[0], end=' ')
