maior = 0
menor = 0
for kilos in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(kilos)))
    if kilos == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else:
            if peso < menor:
                menor = peso
print('')
print('O maior peso foi {}, e o menor foi {}'.format(maior, menor))