d = 0
n = int(input('Digite um número: '))
for c in range(1, n):
    if n % c == 0: #o número digitado vai sendo testado por cada elemento do conjunto
        d = d + 1 #também pode ser "d +=1"
if d > 2:
    print('O número não é primo')
else:
    print('O número é primo')
