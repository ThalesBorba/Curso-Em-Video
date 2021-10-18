from random import randint
from time import sleep
list = []
print('-'*25)
print(f'{"MEGA SENA":^25}')
print('-'*25)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'SORTEANDO {n} JOGOS', '-='*3)
for c in range(1, n+1):
    while True:
        num = randint(0, 60)
        if num not in list:
            list.append(num)
        if len(list) == 6:
            break
    print(f'Jogo {c}: ', list)
    list.clear()
    sleep(2)
print('-='*3, 'BOA SORTE', '-='*3)

