print('-='*5, 'TABUADA', '-='*5)
while True:
    print()
    n = int(input('Digite um número positivo para ver sua tabuada: '))
    print()
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:2} = {c * n}')
print('Tabuada finalizada!')
