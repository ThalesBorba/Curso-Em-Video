n = 0
for c in range(1, 7):
    c = int(input('Digite um número: '))
    if c % 2 == 0:
        n = n + c
print('A soma dos números pares é {}'.format(n))