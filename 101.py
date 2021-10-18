from datetime import date


def votação(ano):
    print(f'Com {a} anos: ', end='')
    if 16 >= a < 18 or a > 65:
        print('Voto opcional.')
    elif a < 16:
        print('Não vota.')
    else:
        print('Voto obrigatório.')


b = int(input('Em que ano você nasceu? '))
a = date.today().year - b
votação(a)