from time import sleep
from random import randint
tentativas = 1
num = randint(0, 10)
numusu = int(input('Em que número de 0 a 10 estou pensando? '))
print('PROCESSSANDO...')
sleep(2)
while numusu != num:
    print('Você errou, o número que pensei foi {}'.format(num))
    num = randint(0, 10)
    numusu = int(input('Tente Novamente! Em que número de 0 a 10 estou pensando? '))
    print('PROCESSSANDO...')
    sleep(2)
    tentativas += 1
print('Muito bem! Você acertou, após {} tentativas!'.format(tentativas))

