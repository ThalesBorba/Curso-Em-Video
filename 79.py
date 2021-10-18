lista = list()
while True:
    elemento = int(input('Digite um valor: '))
    if elemento in lista:
        print('Valor duplicado! Não será incluído!')
    else:
        lista.append(elemento)
    escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Escolha inválida. Quer continuar? [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
print()
print(f'Os valores digitados foram {sorted(lista)}')