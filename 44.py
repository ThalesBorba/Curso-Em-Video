print('=-' * 10)
print('Favor digitar o valor de sua compra e forma de pagamento')
print('1 - À vista no dinheiro ou cheque')
print('2 - À vista no cartão')
print('3 - Em 2X no cartão')
print('4 - Em 3 ou mais vezes no cartão')
print('=-' * 10)
valor = float(input('Valor: '))
cond = int(input('Escolha a condição de pagamento: '))
if cond == 1:
    print('O valor da sua compra ficou em {}'.format(valor * 0.9))
elif cond == 2:
    print('O valor da sua compra ficou em {}'.format(valor * 0.95))
elif cond == 3:
    print('O valor da sua compra ficou em {}'.format(valor))
elif cond == 4:
    print('O valor da sua compra ficou em {}'.format(valor * 1.2))
