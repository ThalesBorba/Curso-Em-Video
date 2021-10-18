extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
posição = int(input('Digite um número entre 0 e 20: '))
while posição not in range(0, 20):
    posição = int(input('Escolha inválida! Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[posição]}')
