from random import randint
from time import sleep
num = randint(0, 5)
numusu = int(input('Em que número de 0 a 5 estou pensando? '))
print('PROCESSSANDO...')
sleep(2)
if numusu == num:
    print('Muito bem! Você acertou!')
else:
    print('Você errou, o número que pensei foi {}'.format(num))
