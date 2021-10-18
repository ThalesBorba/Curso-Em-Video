from time import sleep
maior = 0
print('------- Calculadora pytohn -------' '\n')
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
operação = ''
while operação != 5:
    print('\n' 'Escolha uma das operações abaixo:' '\n [1] Somar' '\n [2] Multiplicar'
          '\n [3] Maior' '\n [4] Novos números' '\n [5] Sair do programa' '\n')
    operação = int(input('Qual operação deseja realizar? '))
    if operação == 1:
        print('A soma entre {} e {} é igual a {}'.format(valor1, valor2, valor1 + valor2))
    elif operação == 2:
        print('O produto de {} por {} é igual a {}'.format(valor1, valor2, valor1 * valor2))
    elif operação == 3:
        if valor1 == valor2:
            print('Os valores são iguais')
        elif valor2 > valor1:
            maior = valor2
            print('O maior valor entre {} e {} é {}'.format(valor1, valor2, maior))
        else:
            maior = valor1
            print('O maior valor entre {} e {} é {}'.format(valor1, valor2, maior))
    elif operação == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif operação == 5:
        print('Finalizando...')
    else:
        print('Operação inválida, tente novamente!')
    sleep(3)
print('Fim do programa!')

