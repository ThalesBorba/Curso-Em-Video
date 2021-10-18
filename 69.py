print('=-'*5, 'SISTEMA DE CADASTRO', '=-'*5)
print()
c = h = m = 0
while True:
    idade = int(input('Digite a idade: '))
    while idade not in range(1, 100):
        idade = int(input('Digite uma idade válida: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Escolha M ou F: ')).upper().strip()[0]
    if idade > 18:
        c += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Escolha S ou N: ')).upper().strip()[0]
    if escolha == 'N':
        break
print('\n'f'Análise completa.')
print(f'Temos {c} pessoas com mais de 18 anos, {h} homem(ns) e {m} mulher(es) com menos de 20 anos')