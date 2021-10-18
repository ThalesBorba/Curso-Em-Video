matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
maior = 0
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor de {l, c}: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print()
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')