c = 0
num1 = 0
num2 = 1
num3 = 0
termos = int(input('Quantos termos deseja ver? '))
while c < termos:
    print(num1, ' -> ', end='')
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    c += 1
print('FIM')