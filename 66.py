c = s = n = 0
while n != 999:
    n = int(input('Digite um número [999 para terminar]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números e a soma deles foi {s}')
