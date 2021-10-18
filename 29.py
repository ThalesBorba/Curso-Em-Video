speed = int(input('A que velocidade estamos? '))
if speed <= 80:
    print('Estamos bem!')
else:
    print('Você ultrapassou o limite de velocidade e foi multado em R${:.2f}'.format((speed - 80)* 7))