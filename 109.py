import úteis
r = 'R$'
n = int(input('Digite o preço: R$'))
print(f'A metade de {úteis.moeda(n)} é {úteis.metade(n, True)}')
print(f'O dobro de {úteis.moeda(n)} é {úteis.dobro(n, True)}')
print(f'Aumentando 10% dá R${úteis.dezpc(n, True)}')