c = -1
s = 0
n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    c += 1
    s += n
print('Você digitou {} números, e a soma entre eles é igual a {}'.format(c, s - 999))
