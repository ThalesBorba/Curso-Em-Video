print('Gerador de PA')
print('-='*10)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
c = 0
total = 0
extra = ''
while c <= 10:
    print(c * razão + termo, ' -> ', end='')
    c += 1
print('PAUSA')
while extra !=0:
    extra = int(input('Quantos termos vc quer mostrar a mais? '))
    total = c + extra -1
    while c <= total:
        print(c * razão + termo, ' -> ', end='')
        c += 1
    print('PAUSA')
print('Progressão terminada com {} termos mostrados'.format(total))