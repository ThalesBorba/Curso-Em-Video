def ficha(d='<desconhecido>', c=0):
    print(f'O jogador {d} fez {c} gol(s) no campeonato.')


a = str(input('Nome do jogador: '))
b = str(input('Número de gols: '))
if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == '':
    ficha(c=b)
else:
    ficha(a, b)
