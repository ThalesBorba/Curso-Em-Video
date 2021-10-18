list = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º número: '))
    if n % 2 == 0:
        list[0].append(n)
    else:
        list[1].append(n)
list[0].sort()
list[1].sort()
print()
print(f'Os valores pares digitados foram {list[0]}')
print(f'Os valores ímpares digitados foram {list[1]}')

