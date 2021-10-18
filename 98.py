from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    print('-='*10)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim < inicio:
        passo = passo * -1
        fim = fim - 1
    else:
        passo = passo
        fim = fim + 1
    for c in range(inicio, fim, passo):
        print(f'{c} ', end='')
        sleep(1)
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
