maior = float(input('Peso da 1ª pessoa: '))
menor = maior
for peso in range(1, 5):
    kilos = float(input('Peso da {}ª pessoa: '.format(peso + 1)))
    if kilos > maior:
        maior = kilos
    else:
        menor = kilos
print('O maior peso foi {}, e o menor foi {}'.format(maior, menor))