frase = input('digite uma frase: ')
letra_procurada = input('digite uma letra: ')

contagem = 0

for letra in frase:
    if letra == letra_procurada:
        contagem += 1

# uma alternativa mais simples é:
# contagem = frase.count(letra_procurada)

print('A letra', letra_procurada, 'apareceu', contagem, 'na frase inserida.')