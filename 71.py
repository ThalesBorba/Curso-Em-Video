c50 = c20 = c10 = c1 = 0
escolha = 'S'
while escolha == 'S':
    d = int(input('Quanto deseja sacar? R$'))
    print()
    while d > 50:
        d -= 50
        c50 += 1
        if d < 50:
            break
    while d > 20:
        d -= 20
        c20 += 1
        if d < 20:
            break
    while d > 10:
        d -= 10
        c10 += 1
        if d < 10:
            break
    while d > 0:
        d -= 1
        c1 += 1
    print('No total você receberá:')
    if c50 != 0:
        print(f'{c50} nota(s) de 50')
    if c20 != 0:
        print(f'{c20} nota(s) de 20')
    if c10 != 0:
        print(f'{c10} nota(s) de 10')
    if c1 != 0:
        print(f'{c1} nota(s) de 1')
    print()
    escolha = str(input('Deseja fazer outro saque? [S/N]: ')).upper().strip()[0]
    print()
    if escolha == 'N':
        break
print('Obrigado por escolher nosso banco!')
