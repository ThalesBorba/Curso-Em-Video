exp = str(input('Digite a expressão: '))
parenteses = []
for simb in exp:
    if simb == '(':
        parenteses.append('(')
    elif simb == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append('(')
            break
if len(parenteses) == 0:
    print('certo')
else:
    print('errado')