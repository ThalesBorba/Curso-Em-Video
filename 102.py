def fatorial(num):
    b = 1
    for c in range(num, 1, -1):
        print(f'{c} x ', end='')
        b *= c
    print(f'1 = {b}')


a = int(input('Digite um número: '))
fatorial(a)