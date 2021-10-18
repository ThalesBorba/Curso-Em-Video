idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você ainda vai se alistar daqui a {} anos'.format(18 - idade))
elif idade > 18:
    print('Você já passou do tempo de alistamento há {} anos'.format(idade - 18))
else:
    print('Está na hora de se alistar')