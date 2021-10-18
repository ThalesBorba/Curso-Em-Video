cadastro = {}
gols = []
cadastro['nome'] = str(input('Nome do jogador: '))
cadastro['partidas'] = int(input(f'Quantaas partidas o {cadastro["nome"]} jogouu? '))
for c in range(0, (cadastro['partidas'])):
    gols.append(int(input('gols')))
cadastro['gols'] = gols[:]
print(cadastro)