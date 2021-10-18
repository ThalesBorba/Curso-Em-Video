time = []
jogador = {}
gols = []
total = dados = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
        total += gols[c]
    jogador['total'] = total
    jogador['gols'] = gols[:]
    time.append(jogador.copy())
    gols.clear()
    total = 0
    escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
    print()
print()
print(f'{"cod":5} {"nome":12} {"gols":20} {"total":5}')
print('-'*50)
for c in range(0, len(time)):
    print(f'{c:<5} {time[c]["nome"]:12} {str(time[c]["gols"]):20} {time[c]["total"]:5}')
print('-'*50)
print()
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    while dados >= len(time) and dados != 999:
        dados = int(input('Escolha inválida! Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {time[dados]["nome"]}')
    for c in range(0, len(time[dados]["gols"])):
        print(f'No jogo {c+1} fez {time[dados]["gols"][c]}')
    print()
print()
print('Valeu, falou')