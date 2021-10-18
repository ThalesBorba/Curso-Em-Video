frase = str(input("Digite a frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for conjunto in range(len(junto) -1, -1, -1):
    inverso += junto[conjunto]
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

