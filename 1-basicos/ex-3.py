quantidade = int(input('Digite a quantidade de números: '))
numeros = []

for i in range(quantidade):
    numero = int(input('Digite o ' + str(i+1) + 'º número: '))
    numeros.append(numero)

soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)

print('A média dos números informados é', media)