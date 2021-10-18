num = int(input('Digite um número para calcular seu fatorial: '))
multiplicação = 1
for fatorial in range(num, 1, -1):
    multiplicação *= fatorial
    print(fatorial, ' X ', end='')
print('1 = {}'.format(multiplicação))