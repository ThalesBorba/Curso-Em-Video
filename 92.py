from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
cadastro['Nascimento'] = int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('Código CTPS [0, se não possuir]: '))
cadastro['Idade'] = datetime.now().year - cadastro['Nascimento']
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = int(input('Salário: R$'))
    cadastro['Anos para aponsendoria'] = (60 - cadastro['Idade']) - ((40 - (datetime.now().year - cadastro['Contratação'])) / 2)
print('-='*20)
for a, b in cadastro.items():
    print(f'{a}: {b}')

