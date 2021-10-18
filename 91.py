from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
print()
for a, b in jogo.items():
    print(f'{a} tirou {b} no dado.')
    sleep(1)
print()
print(f'{" RANKING ":=^15}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for a, b in enumerate(ranking):
    print(f'{a+1}º lugar: {b[0]} com {b[1]}')
    sleep(1)

