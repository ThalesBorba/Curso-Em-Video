escolha = 'S'
c = soma = maior = 0
menor = 0
while escolha in 'Ss':
    n = int(input('Digite um número: '))
    c += 1
    soma += n
    if c == 1:
        menor = n
    if n > maior:
        maior = n
    else:
        if n < menor:
            menor = n
    escolha = str(input('Quer continuar? '))
print('Você digitou {} números, e a média foi {:.2f}'.format(c, soma/c))
print('O maior valor foi {}, e o menor foi {}'.format(maior, menor))
