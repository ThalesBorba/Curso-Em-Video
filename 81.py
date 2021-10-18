lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Escolha inválida. Deseja continuar? [S/N]: ')).upper().strip()[0]
    if escolha in 'Nn':
        break
print()
print(f'VocÊ digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'São eles em ordem decrescente: {lista}')
print('O número 5 ', end='')
if 5 not in lista:
    print('não ', end='')
print('estava na lista')