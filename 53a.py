frase = str(input("Digite a frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('Palíndromo')
else:
    print('Não')