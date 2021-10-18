total = c = c2 = barato = 0
nome = escolha = ''
print('{:-^40}'.format('NOTA FISCAL'))
while True:
    print()
    produto = str(input('Digite o produto: '))
    c2 += 1
    preço = int(input('Digite o preço: R$'))
    total += preço
    if c2 == 1 or preço <= barato:
        barato = preço
        nome = produto
    if preço > 1000:
        c += 1
    escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
print()
print(f'O valor total da compra foi {total:.2f}')
print(f'No total foram {c} produtos que custavam mais de R$1000,00')
print(f'O produto mais barato foi o(a) {nome}, custando R${barato:.2f}')
