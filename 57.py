nome = ''
nome = str(input('Digite seu sexo [M/F]: '))
while nome not in 'FM':
    print('Resposta inválida, tente novamente.')
    nome = str(input('Digite seu sexo [M/F]: '))
