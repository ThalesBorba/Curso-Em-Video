def notas(*n, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas
    :param sit: avaliação da média
    :return: dicionário com informações do aluno
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(9, 10, 5, 7, sit=True)
print(resp)
help(notas)