lista = list()
menor = maior = 0
for cont in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {cont}: ')))
    if cont == 0:
        menor = maior = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for posição, elemento in enumerate(lista):
    if elemento == maior:
        print(f'{posição}... ', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for posição, elemento in enumerate(lista):
    if elemento == menor:
        print(f'{posição}... ', end='')