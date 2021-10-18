print('Gerador de PA')
print('-='*10)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
c = 0
total = 0
extra = 10
while extra != 0:
    total += extra
    while c <= total:
        print(c * razão + termo, ' -> ', end='')
        c += 1
    print('PAUSA')
    extra = int(input('Quantos termos a mais você quer mostrar? '))
print('Progressão terminada com {} termos mostrados'.format(total))