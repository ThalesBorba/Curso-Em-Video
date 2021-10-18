listatodos = []
listapares = []
listaimpares = []
while True:
    n = int(input('Digite um número: '))
    listatodos.append(n)
    if n % 2 == 0:
        listapares.append(n)
    else:
        listaimpares.append(n)
    escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
print('Números: ', listatodos)
print('Pares: ', listapares)
print('Ímpares: ', listaimpares)
