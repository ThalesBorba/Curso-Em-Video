matriz = [[], [], []]
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]: '))
    matriz[0].append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [1, {c}]: '))
    matriz[1].append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [2, {c}]: '))
    matriz[2].append(n)
print(matriz[0])
print(matriz[1])
print(matriz[2])
