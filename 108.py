import úteis
r = 'R$'
n = int(input('Digite o preço: R$'))
print(f'A metade de {úteis.moeda(n)} é {úteis.moeda(úteis.metade(n))}')
print(f'O dobro de {úteis.moeda(n)} é {úteis.moeda(úteis.dobro(n))}')
print(f'Aumentando 10% dá R${úteis.moeda(úteis.dezpc(n))}')
