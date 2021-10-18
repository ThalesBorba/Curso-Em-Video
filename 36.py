print('=-' * 10)
print('EMPRÉSTIMOS FINANCEIRA')
print('=-' * 10)
valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite em quantos anos pretende pagar: '))
mensalidade = valorcasa / anos / 12
if salario * 0.3 < mensalidade:
    print('Prezado cliente, infelizmente seu empréstimo foi negado.')
else:
    print('Parabéns, seu empréstimo foi aprovado e a prestação mensal ficou no valor de R${:.2f}'.format(mensalidade))