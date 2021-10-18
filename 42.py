r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('Esse é um triângulo equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Esse triângulo é escaleno')
    else:
        print('Esse triângulo é isósceles')
else:
    print('Essas retas não formam um triângulo')
