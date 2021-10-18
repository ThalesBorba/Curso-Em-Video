def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nO maior valor foi {maior}')


maior(2, 4, 7, 5, 8, 3)