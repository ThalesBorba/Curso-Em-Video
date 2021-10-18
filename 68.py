from random import randint
from time import sleep
c = n1 = n2 = soma = 0
print('-='*5, 'PAR OU ÍMPAR', '-='*5, '\n')
while True:
    n1 = randint(0, 10)
    n2 = int(input('Digite um número: '))
    r = str(input('PAR OU ÍMPAR [P/I]: ')).upper().strip()
    while r not in 'PpIi':
        r = str(input('Escolha P ou I: ')).upper().strip()
    soma = n1 + n2
    if soma % 2 == 0:
        p = 'P'
        r2 = 'PAR'
    else:
        p = 'I'
        r2 = 'ÍMPAR'
    sleep(2)
    print()
    if p != r:
        break
    if p == r:
        print(f'Eu escolhi {n1}, e a soma deu {soma} ({r2})')
        print('Quero revanche!')
        print()
        c += 1
print(f'Eu escolhi {n1}, e a soma deu {soma} ({r2}).')
print(f'Jogo terminado, você ganhou {c} vezes!')
