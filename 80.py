lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0                         #1 - começando na posição 0
        while pos < len(lista):         #2 - enquanto não chegar no último número, vai comparando
            if n <= lista[pos]:         #3 - vê se o número é menor que o da posição atual
                lista.insert(pos, n)    #4 - se for, encaixa e empurra o outro para a direita
                break                   #5 - e quebra o looping
            pos +=1                     #6 - senão, compara com o da próxima posição
print()
print(f'{lista}')
