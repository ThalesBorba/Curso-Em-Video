list = []
aluno =[]
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    list.append(aluno[:])
    aluno.clear()
    escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while escolha not in 'NS':
        escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
print('-='*20)
print(f'{"No.":<3}', f'{"NOME":<15}', f'{"MÉDIA":>3}')
print('-'*25)
for c in range(0, len(list)):
    print(f'{c:<3}', f'{list[c][0]:<15}', f'{list[c][3]:>4.1f}')
print('-'*25)
while True:
    c = int(input('Deseja mostrar as notas de qual aluno? (999 para encerrar): '))
    if c not in range(0, len(list)-1) and c != 999:
        c = int(input('Escolha inválida, selecione o número do aluno (999 para parar): '))
    if c == 999:
        break
    print(f'As notas do aluno {list[c][0]} foram {list[c][1]} e {list[c][2]}')
    print()
print()
print('Programa finalizado')
